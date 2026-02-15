# AGENT.md - Technical Overview & Workflows

This document serves as the primary technical reference for AI agents working on the Fast Voice-to-Text project.

## Architecture Overview

The system follows a split architecture:

1.  **Lightweight Client (`src/fast_voice/client`)**:
    -   **`core.py`**: The `VoiceClient` class handles audio capture (PyAudio), processing (NumPy), and WebSocket streaming.
    -   **`tui.py`**: Rich-based terminal UI.
    -   **`daemon.py`**: Auto-starts the server if needed.
    -   **Protocol**: Sends binary audio frames; receives JSON transcription events.

2.  **Inference Server (`src/fast_voice/server`)**:
    -   **`server.py`**: WebSocket server (FastAPI/Uvicorn not used for main flow, custom loop).
    -   **`whisper_live/`**: Backend logic wrapping `faster-whisper`.
    -   **VAD**: Integrated Voice Activity Detection.

3.  **Configuration**:
    -   `app.yaml`: Central config file, hot-reloaded every 2 seconds.

## Key Workflows

### 1. Adding New Clients
Refer to `development.md` and `docs/asyncapi.yaml`. Use the `SimulationClient` for headless testing.

### 2. Testing
-   **Unit Tests**: `uv run python -m unittest discover tests` covers client, server, and flow.
-   **E2E**: `tests/test_e2e.py` verifies the full pipeline with synthetic audio.
-   **Monitor**: `tests/test_monitor_e2e.py` verifies browser monitor broadcasting.

### 3. Debugging
-   **Audio**: Use `SimulationClient(audio_file="...")` to inject known audio.
-   **Logs**: Server logs to stderr. Client logs connection status to stderr.
-   **TUI**: Renders to stderr to keep stdout clean for piping.

## Code Standards
-   **Linting**: Follow standard Python practices. No implementation details in comments.
-   **Concurrency**: Use `asyncio` for client I/O. Threading for blocking server inference.
-   **Dependencies**: explicit in `pyproject.toml`.

## Common Pitfalls
-   **Sorting**: Transcription segments must be sorted by `start` time (float), not string, to avoid ordering bugs.
-   **Buffer**: `faster-whisper` requires context; the server manages a rolling audio buffer.
-   **Hot-Reload**: Config changes apply instantly; ensure component re-reads config or handles updates.
