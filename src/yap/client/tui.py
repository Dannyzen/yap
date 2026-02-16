import asyncio
import queue
import sys
from datetime import datetime
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.table import Table

from yap.client.core import VoiceClient

SHORTCUTS = {
    "c": "Copy transcript to clipboard",
    "?": "Toggle this help overlay",
    "Ctrl+C": "Quit and print transcript to stdout",
}

class TUIApp:
    def __init__(self, client=None):
        self.console = Console(stderr=True)  # TUI renders to stderr
        self.client = client if client else VoiceClient()
        self.transcript_queue = queue.Queue()
        self.status = "Disconnected"
        self.status_style = "red"
        self.running = True
        self._last_text = ""
        self._show_help = False

    def make_layout(self) -> Layout:
        layout = Layout(name="root")
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3),
        )
        return layout

    def render_header(self):
        title = Text(" ⚡ Yap ", style="bold white on blue")
        status_text = Text(f" ● {self.status} ", style=f"bold white on {self.status_style}")
        
        return Panel(
            Align.center(title + Text(" ") + status_text),
            style="blue",
            padding=(0, 1)
        )

    def render_main(self):
        if self._show_help:
            return self._render_help()

        # Show the current transcript as one continuous block — no timestamps, no line breaks
        text_content = Text(self._last_text or "Waiting for speech...", 
                          style="bold white" if self._last_text else "dim italic")
        
        return Panel(
            text_content,
            title="Live Transcription",
            border_style="green"
        )

    def _render_help(self):
        table = Table(title="Keyboard Shortcuts", border_style="cyan", expand=True)
        table.add_column("Key", style="bold yellow", width=12)
        table.add_column("Action", style="white")
        
        for key, desc in SHORTCUTS.items():
            table.add_row(key, desc)
        
        return Panel(table, title="Help", border_style="cyan")

    def render_footer(self):
        return Panel(
            Align.center("[bold yellow]c[/] Copy  [bold yellow]?[/] Help  [bold yellow]Ctrl+C[/] Quit"),
            style="dim white",
            padding=(0, 1)
        )

    def on_transcribed(self, text):
        """Callback from VoiceClient — receives the full compiled text each update."""
        if text:
            self.transcript_queue.put(text)
            self._last_text = text

    def copy_to_clipboard(self):
        try:
            import pyperclip
            if self._last_text:
                pyperclip.copy(self._last_text)
                self.status = "Copied!"
                self.status_style = "magenta"
                self._status_timer = 20  # Show for ~2 seconds (20 * 0.1s)
            else:
                 self.status = "Nothing to copy"
                 self.status_style = "yellow"
                 self._status_timer = 10
        except Exception as e:
            self.status = "Copy Failed"
            self.status_style = "red"
            self._status_timer = 20
            # Import might fail if xclip/xsel missing on Linux

    async def run(self):
        # ... (setup layout) ...
        self.status = "Connecting..."
        self.status_style = "yellow"
        self._status_timer = 0
        
        # ... (client task) ...
        client_task = asyncio.create_task(
            self.client.run(
                duration=999999,
                on_transcription=self.on_transcribed,
                on_live_update=self.on_transcribed
            )
        )

        self.status = "Listening"
        self.status_style = "green"

        import tty, termios, select
        old_settings = None
        fd = sys.stdin.fileno()
        
        try:
            old_settings = termios.tcgetattr(fd)
            tty.setcbreak(fd)
        except Exception:
            pass

        try:
            with Live(self.make_layout(), refresh_per_second=10, screen=True, console=self.console) as live:
                while self.running:
                    # 1. Update Transcript
                    while not self.transcript_queue.empty():
                        try:
                            self._last_text = self.transcript_queue.get_nowait()
                        except queue.Empty:
                            break
                    
                    # 2. Handle Input
                    if old_settings:
                        rlist, _, _ = select.select([sys.stdin], [], [], 0)
                        if rlist:
                            ch = sys.stdin.read(1)
                            if ch == 'c':
                                self.copy_to_clipboard()
                            elif ch == '?':
                                self._show_help = not self._show_help
                            elif ch == '\x03': # Ctrl+C
                                self.running = False

                    # 3. Status Timer Logic
                    if self._status_timer > 0:
                        self._status_timer -= 1
                        if self._status_timer == 0:
                            self.status = "Listening"
                            self.status_style = "green"

                    # 4. Render
                    # (Construct layout updates manually to avoid attribute errors if make_layout returns new obj)
                    # Actually, Live(layout) keeps reference. We need to update that specific layout object.
                    # Use a persistent layout object.
                    
                    # Re-create layout components for update
                    live.update(self._update_layout())
                    
                    await asyncio.sleep(0.1)
                    
                    if client_task.done():
                        self.status = "Disconnected"
                        self.status_style = "red"
                        live.update(self._update_layout())
                        break

        finally:
            if old_settings:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
            # Cancel client if still running
            if not client_task.done():
                client_task.cancel()
                try:
                    await client_task
                except asyncio.CancelledError:
                    pass

        return self._last_text

    def _update_layout(self):
        layout = self.make_layout()
        layout["header"].update(self.render_header())
        layout["main"].update(self.render_main())
        layout["footer"].update(self.render_footer())
        return layout

def main():
    app = TUIApp()
    final_text = ""
    try:
        final_text = asyncio.run(app.run())
    except KeyboardInterrupt:
        final_text = app._last_text
    finally:
        # Single clean line to stdout
        if final_text:
            print(final_text, file=sys.stdout)

if __name__ == "__main__":
    main()
