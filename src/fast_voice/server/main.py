import logging
from fast_voice.config import Config
from fast_voice.whisper_live.server import TranscriptionServer
from fast_voice.whisper_live.backend.faster_whisper_backend import ServeClientFasterWhisper

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')

def start():
    print("⚡ Fast Voice-to-Text Daemon (v2td) starting...")
    config = Config()
    
    # Load config values
    port = config.get("server.port", 9090)
    host = config.get("server.host", "0.0.0.0")
    model_size = config.get("model.size", "small")
    
    # 1. Warmup Model
    try:
        ServeClientFasterWhisper.preload_model(model_size)
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
