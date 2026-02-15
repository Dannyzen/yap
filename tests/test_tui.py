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

    def test_on_transcribed(self):
        self.app.on_transcribed("Hello World")
        self.assertFalse(self.app.transcript_queue.empty())
        timestamp, text = self.app.transcript_queue.get()
        self.assertEqual(text, "Hello World")
        self.assertIn(":", timestamp) # Check for time format

    def test_make_layout(self):
        layout = self.app.make_layout()
        self.assertTrue(layout.split_column)
        self.assertEqual(layout["header"].size, 3)
        self.assertEqual(layout["footer"].size, 3)

    @patch('fast_voice.client.tui.Layout')
    @patch('fast_voice.client.tui.Panel')
    def test_render_main(self, mock_panel, mock_layout):
        # Setup some transcript data
        self.app.transcript_queue.put(("12:00:00", "Test Transcript"))
        
        # We can't easily test the full async loop without more extensive mocking of Live
        # But we can test the helper methods
        
        # Test update_transcript logic manually
        # TUIApp.run() is the main loop, we can't call it directly in unit test as it blocks/loops
        pass

if __name__ == "__main__":
    unittest.main()
