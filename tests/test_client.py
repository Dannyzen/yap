import unittest
from unittest.mock import patch, AsyncMock
import asyncio
from yap.client.core import VoiceClient

class TestVoiceClient(unittest.TestCase):
    def setUp(self):
        # Mock ensure_daemon_running to prevent actual subprocess calls
        self.daemon_patcher = patch('yap.client.core.ensure_daemon_running')
        self.mock_ensure_daemon = self.daemon_patcher.start()
        
        # Mock PyAudio
        self.pyaudio_patcher = patch('yap.client.core.pyaudio')
        self.mock_pyaudio = self.pyaudio_patcher.start()
        
        # Mock Config
        self.config_patcher = patch('yap.client.core.Config')
        self.mock_config = self.config_patcher.start()
        self.mock_config.return_value.get.return_value = 'default'

    def tearDown(self):
        self.daemon_patcher.stop()
        self.pyaudio_patcher.stop()
        self.config_patcher.stop()

    def test_init(self):
        client = VoiceClient(host='localhost', port=9090)
        self.assertEqual(client.rate, 32000)
        self.mock_ensure_daemon.assert_called_with('localhost', 9090)

    @patch('yap.client.core.websockets.connect')
    def test_run_handshake(self, mock_ws_connect):
        async def run_test():
            client = VoiceClient()
            
            # Mock websocket context manager
            mock_ws = AsyncMock()
            mock_ws_connect.return_value.__aenter__.return_value = mock_ws
            
            # Mock recv sequence: SERVER_READY -> Stop
            # We mock send_audio to return immediately (via stop_event check or exception)
            # Actually, run() waits for SERVER_READY then records.
            mock_ws.recv.side_effect = [
                '{"message": "SERVER_READY"}',
                asyncio.CancelledError # Break loop if needed or just hang
            ]
            
            # Mock send_audio to exit fast
            client.send_audio = AsyncMock()
            
            try:
                # Run for 0.1s
                await client.run(duration=0.1)
            except Exception:
                pass
            
            # Verify handshake sent
            handshake_call = mock_ws.send.call_args_list[0]
            import json
            handshake = json.loads(handshake_call[0][0])
            self.assertEqual(handshake['task'], 'transcribe')
            self.assertEqual(handshake['use_vad'], True)

        asyncio.run(run_test())

    def test_run_handshake_auto_start_check(self):
        """Verify explicit auto_start=False works"""
        client = VoiceClient(auto_start=False)
        self.mock_ensure_daemon.assert_not_called()

if __name__ == '__main__':
    unittest.main()
