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
from rich.style import Style

from fast_voice.client.core import VoiceClient

class TUIApp:
    def __init__(self, client=None):
        self.console = Console(stderr=True)  # TUI renders to stderr
        self.client = client if client else VoiceClient()
        self.transcript_queue = queue.Queue()
        self.full_transcript = []
        self.status = "Disconnected"
        self.status_style = "red"
        self.running = True
        self._last_text = ""

    def make_layout(self) -> Layout:
        """Define the grid."""
        layout = Layout(name="root")
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3),
        )
        return layout

    def render_header(self):
        """Render standard header with status."""
        grid = Layout()
        grid.split_row(
            Layout(name="title", ratio=3),
            Layout(name="status", ratio=1)
        )
        
        title = Text(" ⚡ Fast Voice-to-Text ", style="bold white on blue")
        status_text = Text(f" ● {self.status} ", style=f"bold white on {self.status_style}")
        
        return Panel(
            Align.center(title if self.status == "Disconnected" else title + Text(" ") + status_text),
            style="blue",
            padding=(0, 1)
        )

    def render_main(self):
        """Render the scrolling transcript."""
        # Join all segments
        text_content = Text()
        for timestamp, text in self.full_transcript[-15:]: # Show last 15 items
            text_content.append(f"[{timestamp}] ", style="dim cyan")
            text_content.append(f"{text}\n", style="bold white")
            
        return Panel(
            text_content,
            title="Live Transcription",
            border_style="green"
        )

    def render_footer(self):
        return Panel(
            Align.center("[bold]c[/bold] Copy | [bold]CTRL+C[/bold] Quit | [bold]Listening[/bold] on default device"),
            style="dim white",
            padding=(0, 1)
        )

    def on_transcribed(self, text):
        """Callback from VoiceClient (Background Thread)"""
        if text:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.transcript_queue.put((timestamp, text))
            self._last_text = text

    def copy_to_clipboard(self):
        """Copy current transcript to clipboard."""
        try:
            import pyperclip
            if self._last_text:
                pyperclip.copy(self._last_text)
                self.status = "Copied!"
                self.status_style = "magenta"
        except ImportError:
            self.status = "pyperclip not installed"
            self.status_style = "red"

    async def run(self):
        layout = self.make_layout()
        
        self.status = "Connecting..."
        self.status_style = "yellow"
        
        client_task = asyncio.create_task(
            self.client.run(
                duration=999999, # Run "forever"
                on_live_update=self.on_transcribed
            )
        )

        self.status = "Listening"
        self.status_style = "green"

        # Keyboard listener (non-blocking)
        import selectors, tty, termios, os
        old_settings = None
        try:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            tty.setcbreak(fd)
        except Exception:
            pass

        with Live(layout, refresh_per_second=10, screen=True, console=self.console) as live:
            while self.running:
                # 1. Process new messages
                while not self.transcript_queue.empty():
                    try:
                        ts, txt = self.transcript_queue.get_nowait()
                        self.full_transcript.append((ts, txt))
                    except queue.Empty:
                        break
                
                # 2. Check for keypress (non-blocking)
                if old_settings is not None:
                    import select
                    rlist, _, _ = select.select([sys.stdin], [], [], 0)
                    if rlist:
                        ch = sys.stdin.read(1)
                        if ch == 'c':
                            self.copy_to_clipboard()

                # 3. Update Layout
                layout["header"].update(self.render_header())
                layout["main"].update(self.render_main())
                layout["footer"].update(self.render_footer())
                
                # Reset status after copy notification
                if self.status == "Copied!":
                    await asyncio.sleep(1)
                    self.status = "Listening"
                    self.status_style = "green"
                
                await asyncio.sleep(0.1)
                
                if client_task.done():
                    self.status = "Disconnected"
                    self.status_style = "red"
                    break

        # Restore terminal
        if old_settings is not None:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return self._last_text

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
