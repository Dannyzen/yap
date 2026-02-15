import unittest
from unittest.mock import MagicMock, patch, AsyncMock
import queue
from fast_voice.client.tui import TUIApp

class TestTUI(unittest.TestCase):
    def setUp(self):
        # Patch Environment to prevent ALSA/PyAudio issues
        self.pyaudio_patcher = patch('fast_voice.client.core.pyaudio')
        self.pyaudio_patcher.start()
        self.ctypes_patcher = patch('ctypes.CFUNCTYPE')
        self.ctypes_patcher.start()
        self.cdll_patcher = patch('ctypes.cdll')
        self.cdll_patcher.start()
        
        self.mock_client = MagicMock()
        self.mock_client.connect = AsyncMock()
        self.mock_client.start_stream = AsyncMock()
        self.mock_client.close = AsyncMock()
        
        # Patch Console to avoid actual printing
        self.console_patcher = patch('fast_voice.client.tui.Console')
        self.mock_console = self.console_patcher.start()
        self.app = TUIApp(self.mock_client)

    def tearDown(self):
        self.console_patcher.stop()
        self.pyaudio_patcher.stop()
        self.ctypes_patcher.stop()
        self.cdll_patcher.stop()

    def test_initialization(self):
        self.assertIsInstance(self.app.transcript_queue, queue.Queue)
        self.assertEqual(self.app.status, "Disconnected")
        self.assertEqual(self.app._last_text, "")
        self.assertFalse(self.app._show_help)

    def test_on_transcribed(self):
        self.app.on_transcribed("Hello World")
        self.assertFalse(self.app.transcript_queue.empty())
        text = self.app.transcript_queue.get()
        self.assertEqual(text, "Hello World")
        self.assertEqual(self.app._last_text, "Hello World")

    def test_on_transcribed_empty(self):
        self.app.on_transcribed("")
        self.assertTrue(self.app.transcript_queue.empty())

    def test_make_layout(self):
        layout = self.app.make_layout()
        self.assertTrue(layout.split_column)
        self.assertEqual(layout["header"].size, 3)
        self.assertEqual(layout["footer"].size, 3)

    def test_help_toggle(self):
        self.assertFalse(self.app._show_help)
        self.app._show_help = True
        # The help panel renders via _render_help
        panel = self.app.render_main()
        # Should contain "Help" in the title
        self.assertIsNotNone(panel)

if __name__ == "__main__":
    unittest.main()
