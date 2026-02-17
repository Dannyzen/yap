import unittest
from unittest.mock import AsyncMock, Mock, patch
import json
import asyncio
# Avoid top-level import of VoiceClient if it triggers pyaudio
# We will patch pyaudio in setUp

class TestClientFlow(unittest.TestCase):
    def setUp(self):
        self.pyaudio_patcher = patch('yap.client.core.pyaudio')
        self.mock_pyaudio = self.pyaudio_patcher.start()
        
        # Also patch ctypes to avoid alsa error handler logic running
        self.ctypes_patcher = patch('ctypes.CFUNCTYPE')
        self.ctypes_patcher.start()
        self.cdll_patcher = patch('ctypes.cdll')
        self.cdll_patcher.start()
        
        # Patched config to avoid file lookups
        self.config_patcher = patch('yap.client.core.Config')
        self.mock_config = self.config_patcher.start()
        self.mock_config.return_value.get.return_value = "default"

        from yap.client.core import VoiceClient
        self.VoiceClient = VoiceClient

    def tearDown(self):
        self.pyaudio_patcher.stop()
        self.ctypes_patcher.stop()
        self.cdll_patcher.stop()
        self.config_patcher.stop()

    def test_receive_transcription_callback(self):
        """
        Verify that JSON messages from the daemon are correctly parsed 
        and the application callback is invoked with the text.
        """
        client = self.VoiceClient(auto_start=False)
        
        # Mock Websocket
        mock_ws = AsyncMock()
        
        # Define simulation data
        # Sequence of messages simulating live transcription updates
        messages = [
            json.dumps({"segments": [{"start": 0.0, "text": "Hello"}]}),
            json.dumps({"segments": [{"start": 0.0, "text": "Hello"}, {"start": 1.0, "text": "World"}]}),
            # End of stream (handled by loop termination in test)
        ]
        
        # Create an async iterator for the websocket
        async def message_iterator():
            for msg in messages:
                yield msg
            # Simulate connection close or just stop
            
        mock_ws.__aiter__.side_effect = message_iterator
        
        # Mock Callback
        mock_callback = Mock()
        
        # Run receieve_transcription
        # it loops until exception or end. 
        # VoiceClient.receive_transcription catches exceptions but we want to break loop.
        # It relies on "async for message in websocket".
        # So our iterator finishing should be enough?
        # VoiceClient.receive_transcription:
        # async for message in websocket: ...
        # finally: ... callback(final)
        
        # In this synchronous mock, the callback is only called once in the finally block after the async 
        # iterator breaks, which differs from the real-time streaming updates of the actual WebSocket client.
        
        pass 
        # I'll implement the test to Assert this behavior.

        async def run_test():
             await client.receive_transcription(mock_ws, callback=None, on_live_update=mock_callback)
        
        asyncio.run(run_test())
        
        # Verification
        # Should be called 2 times (once per message)
        self.assertEqual(mock_callback.call_count, 2)
        
        # Check args
        args1 = mock_callback.call_args_list[0][0][0]
        self.assertIn("Hello", args1)
        
        args2 = mock_callback.call_args_list[1][0][0]
        self.assertIn("Hello World", args2)

if __name__ == "__main__":
    unittest.main()
