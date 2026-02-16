"""
Yap Server Entry Point.

This module initializes and runs the Transcription Server, loading configuration
from `app.yaml` and warming up the Whisper model.
"""
import logging
from yap.config import Config
from yap.whisper_live.server import TranscriptionServer
from yap.whisper_live.backend.faster_whisper_backend import ServeClientFasterWhisper

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

def start():
    """
    Start the Voice-to-Text Daemon (v2td).
    
    1. Loads configuration from app.yaml
    2. Preloads/Warms up the Whisper model
    3. Starts the WebSocket server
    """
    print("⚡ Yap Daemon (v2td) starting...")
    config = Config()

    # Load config values
    port = config.get("server.port", 9090)
    host = config.get("server.host", "0.0.0.0")
    model_size = config.get("model.size", "small")
    compute_type = config.get("model.compute_type") # Can be None
    # 1. Warmup Model
    try:
        ServeClientFasterWhisper.preload_model(model_size, compute_type=compute_type)
    except Exception as e:
        print(f"FATAL: Model warmup failed: {e}")
        return

    # 2. Start Server
    server = TranscriptionServer()
    print(f"⚡ Daemon Ready. Listening on {host}:{port}")
    print("   (Use 'v2t' to connect)")
    
    server.run(
        host=host,
        port=port,
        backend="faster_whisper",
        single_model=True, # Use the pre-loaded model
    )

if __name__ == "__main__":
    start()
