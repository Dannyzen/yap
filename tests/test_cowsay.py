import unittest
from unittest.mock import MagicMock, patch, AsyncMock
import io
import sys
import os
sys.path.append(os.getcwd()) # Ensure root is in path
from examples.cowsay_app import cowsay, main

class TestCowsayApp(unittest.TestCase):
    def test_cowsay_formatting(self):
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            cowsay("Hello World")
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        self.assertIn("Hello World", output)
        self.assertIn("(oo)", output) # The cow eyes
        
    @patch('examples.cowsay_app.VoiceClient')
    def test_main_loop(self, MockVoiceClient):
        # Setup mock client
        mock_client_instance = MockVoiceClient.return_value
        mock_client_instance.run = AsyncMock()
        
        # Run main
        # We need to make sure it doesn't run forever or block?
        # main() just calls client.run(duration=10)
        # So mocking run is enough.
        
        import asyncio
        asyncio.run(main())
        
        # Verify run called with correct args
        mock_client_instance.run.assert_awaited_once()
        kwargs = mock_client_instance.run.call_args[1]
        self.assertIn('on_transcription', kwargs)
        self.assertTrue(callable(kwargs['on_transcription']))
        
        # Verify callback works
        callback = kwargs['on_transcription']
        
        # Capture stdout for callback execution
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            callback("Test Message")
        finally:
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        self.assertIn("Test Message", output)

if __name__ == "__main__":
    unittest.main()
