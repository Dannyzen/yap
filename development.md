# Development Guide

This guide explains how to develop clients for the **WhisperLive** daemon using our [AsyncAPI 3.0.0 Schema](asyncapi.yaml).

## Protocol Overview

The protocol is simple and consists of three phases:
1.  **Handshake**: Send a JSON configuration object.
2.  **Streaming**: Send binary audio chunks (Client -> Server) and receive JSON transcription events (Server -> Client).
3.  **Termination**: Close the WebSocket.

### Schema
The full schema is defined in `asyncapi.yaml`. You can use [AsyncAPI Tools](https://www.asyncapi.com/tools) to view this interactively or generate code templates.

---

## Tutorial: Building a "Cowsay" Client

In this tutorial, we will build a simple Python client that:
1.  Connects to the daemon.
2.  Listens to your microphone for 5 seconds.
3.  Prints the transcription using an ASCII cow.

### Prerequisites
- Python 3.8+
- `websockets`, `pyaudio`
- Running daemon (`uv run v2td.py`)

### Step 1: The Handshake
According to our schema, the client must send a `Handshake` message immediately upon connection.
```python
handshake = {
    "uid": "unique-id-123",
    "language": "en",
    "task": "transcribe",
    "model": "small"
}
await websocket.send(json.dumps(handshake))
```

### Step 2: Audio Streaming
Audio must be sent as **binary frames**. The server expects raw PCM data (usually 16kHz, 16-bit mono, or float32).
```python
# Send chunks of raw audio bytes
await websocket.send(audio_chunk_bytes)
```

### Step 3: Handling Transcriptions
The server replies with `Transcription` messages.
```json
{
  "uid": "unique-id-123",
  "segments": [
    {
      "start": "0.000",
      "end": "2.500",
      "text": "Hello world",
      "completed": false
    }
  ]
}
```

### Full Example Code (`cowsay_client.py`)

See `cowsay_client.py` for the complete implementation. Run it with:

```bash
uv run cowsay_client.py
```

### Expected Output

```text
Connecting to ws://localhost:9090...
Server is ready! Speak now (5 seconds)...

Stopped recording. Waiting for final transcription...

 ___________________________
< Hello world, this is a de >
< mo of the cowsay client.  >
 ---------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
