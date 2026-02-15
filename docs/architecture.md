# Fast Voice-to-Text Architecture

## Overview
Fast Voice-to-Text is a split-architecture system designed for low-latency, high-fidelity speech recognition using `faster-whisper`. It separates the heavy inference engine (Server) from the lightweight audio capture (Client).

## Components

### 1. Client (`src/fast_voice/client`)
- **Core Logic**: `VoiceClient` (in `core.py`) handles:
    - **Audio Capture**: Uses `pyaudio` to capture raw PCM data.
    - **Device Management**: Auto-selects input devices (e.g., C920 Webcam) based on config.
    - **Signal Processing**:
        - Downmixes Stereo to Mono.
        - Downsamples (e.g., 32kHz -> 16kHz) using `numpy`.
        - Normalizes Int16 to Float32 (-1.0 to 1.0).
    - **Communication**: Streams audio over WebSocket to the Server.
- **Daemon Management**: `ensure_daemon_running` auto-launches the server if not detected.

### 2. Server (`src/fast_voice/server`)
- **Entry Point**: `fast-voice-server` (wraps `main.py`).
- **Backend**: Uses `faster-whisper` for inference.
- **Protocol**: Websocket-based. Accepts Float32 raw audio, returns JSON partial/final transcripts.
- **VAD**: Integrated Voice Activity Detection to filter silence before inference.

### 3. Shared Library (`src/fast_voice/whisper_live`)
- Legacy core logic from `whisper-live` project.
- Handles VAD, buffering, and tensor operations.

## Configuration
Managed by `app.yaml`.
- **Audio**: Sample rate, input device index.
- **Model**: Size (tiny/base/small), language, compute type (int8/float16).
- **Server**: Host/Port.

## Directory Structure
```text
src/fast_voice/
├── client/          # Lightweight capture & network logic
├── server/          # Inference engine & daemon
├── whisper_live/    # Shared backend components
└── config.py        # Central configuration loader
examples/            # Example applications (cowsay_app.py)
tests/               # Unit tests
docs/                # Documentation
```
