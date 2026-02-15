# Development Guide

Build custom voice-to-text clients using the Fast Voice daemon and its WebSocket API.

## Architecture

```
┌──────────────┐    WebSocket    ┌──────────────────┐
│  Your Client │ ◄────────────► │  fast-voice-server │
│  (Lightweight)│   Binary Audio │  (Daemon)          │
│              │   JSON Results  │  faster-whisper    │
└──────────────┘                └──────────────────┘
```

The daemon handles all heavy lifting (model loading, VAD, inference). Your client only needs to:
1. Open a WebSocket to `ws://localhost:9090`
2. Send a JSON handshake
3. Stream raw audio bytes
4. Parse JSON transcription responses

## Protocol Reference

The full protocol is defined in [`docs/asyncapi.yaml`](docs/asyncapi.yaml) (AsyncAPI 3.0.0).

### Phase 1: Handshake
```json
{
  "uid": "unique-client-id",
  "language": "en",
  "task": "transcribe",
  "model": "small",
  "use_vad": true,
  "initial_prompt": "optional context for the model"
}
```

### Phase 2: Wait for `SERVER_READY`
```json
{ "uid": "...", "message": "SERVER_READY", "backend": "faster_whisper" }
```

### Phase 3: Stream Audio
Send raw audio as **binary WebSocket frames**. Expected format:
- 16kHz sample rate
- Float32 or Int16
- Mono channel

### Phase 4: Receive Transcriptions
```json
{
  "uid": "...",
  "segments": [
    { "start": "0.000", "end": "2.500", "text": "Hello world", "completed": false }
  ]
}
```

Segments update in real-time. Use the `start` field as a key to deduplicate updates for the same segment.

### Error Handling
```json
{ "uid": "...", "status": "ERROR", "message": "description" }
```

---

## Using the Python SDK

The fastest way to build a client:

```python
import asyncio
from fast_voice.client.core import VoiceClient

async def main():
    client = VoiceClient()  # Auto-starts daemon if not running

    # Final callback — called once when recording ends
    def on_done(text):
        print(f"Final: {text}")

    # Live callback — called on every segment update
    def on_update(text):
        print(f"Live: {text}")

    await client.run(
        duration=10,
        on_transcription=on_done,    # Final text
        on_live_update=on_update      # Real-time updates
    )

asyncio.run(main())
```

### SDK Callbacks

| Parameter | When Called | Use Case |
|---|---|---|
| `on_transcription` | Once, after recording ends | Cowsay, clipboard, file output |
| `on_live_update` | On every segment update | TUI, browser monitor, live display |

---

## Auto-Starting the Daemon

`VoiceClient` automatically starts `fast-voice-server` if it can't connect. This is handled by `ensure_daemon_running()` in `client/daemon.py`. No manual server management needed.

To run the daemon manually (e.g., for debugging):
```bash
uv run fast-voice-server
```

---

## Code Generation with AsyncAPI

The [`docs/asyncapi.yaml`](docs/asyncapi.yaml) schema is a standard [AsyncAPI 3.0.0](https://www.asyncapi.com/) document. You can use AsyncAPI tooling to:

### Generate Client Code
```bash
# Install the AsyncAPI CLI
npm install -g @asyncapi/cli

# Generate a Python client stub
asyncapi generate fromTemplate docs/asyncapi.yaml @asyncapi/python-paho-template -o generated/

# Generate docs
asyncapi generate fromTemplate docs/asyncapi.yaml @asyncapi/html-template -o docs/generated/
```

### Interactive Schema Viewer
```bash
# View the schema interactively in your browser
asyncapi start studio docs/asyncapi.yaml
```

Or paste the YAML into [AsyncAPI Studio](https://studio.asyncapi.com/) online.

---

## Example Clients

| Client | File | Description |
|---|---|---|
| Cowsay | [`examples/cowsay_app.py`](examples/cowsay_app.py) | Records 10s, prints ASCII cow with transcript |
| TUI | [`src/fast_voice/client/tui.py`](src/fast_voice/client/tui.py) | Rich terminal UI with live updates, clipboard |
| Browser | [`src/fast_voice/server/static/index.html`](src/fast_voice/server/static/index.html) | Real-time browser monitor via WebSocket |

---

## Configuration

Edit `app.yaml` (hot-reloaded every 2 seconds):

```yaml
model:
  size: "small"           # tiny | base | small | medium | large-v3
  compute_type: "int8"    # int8 (CPU) | float16 (GPU)
  language: "en"

audio:
  input_device: "default" # Device index or "default"
  use_vad: true

server:
  host: "0.0.0.0"
  port: 9090
```

## Running Tests

```bash
# Full test suite
uv run python -m unittest discover tests

# Individual tests
uv run python -m unittest tests/test_e2e.py
uv run python -m unittest tests/test_client_flow.py
uv run python -m unittest tests/test_tui.py
uv run python -m unittest tests/test_cowsay.py
```
