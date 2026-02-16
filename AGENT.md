# Fast Voice-to-Text Agent Guide

This document is designed to help AI Agents and Developers understand the structure, usage, and internal workings of the **Fast Voice-to-Text** system.

## Project Overview
Fast Voice-to-Text is a split-architecture speech recognition system tailored for low latency and high performance. It offloads heavy inference to a server while keeping the client lightweight.

### Core Components
1.  **Client (`src/fast_voice/client`)**:
    *   Captures audio from the microphone to a buffer.
    *   Resamples audio to 16kHz.
    *   Streams raw PCM data via WebSocket to the server.
    *   Handles "VAD" (Voice Activity Detection) implicitly by only sending audio when requested, or continuous streaming.
2.  **Server (`src/fast_voice/server`)**:
    *   Hosts a WebSocket server (default port 9090).
    *   Receives audio chunks.
    *   Runs `faster-whisper` (an optimized implementation of OpenAI's Whisper).
    *   Performs VAD to filter silence.
    *   Returns partial and final JSON transcripts.
3.  **WebUI (`src/fast_voice/server/static/index.html`)**:
    *   A browser-based client that behaves exactly like the Python client.
    *   Uses Web Audio API (`scriptProcessor`) to capture and downsample audio.
    *   Connects to the server to display real-time results.

## Configuration (`app.yaml`)
The system behaves dynamically based on `app.yaml`.
*   **Model**: Toggle between `tiny`, `small`, `medium`, `large-v2`.
*   **Compute**: `float16` (GPU) or `int8` (CPU). The system auto-downgrades if GPU is missing.
*   **VAD**: Adjust `vad_onset` and `vad_offset` to tune silence detection sensitivity.

## Development Workflow
*   **Run Server**: `uv run v2td`
*   **Run Client**: `uv run fast-voice-client`
*   **Run Web Client**: Open `src/fast_voice/server/static/index.html`
*   **Testing**: `uv run python -m unittest discover tests`

## Key Internal Structures
*   **`ServeClientBase`**: Abstract base class handling the WebSocket loop and buffering.
*   **`ServeClientFasterWhisper`**: Implementation using `faster-whisper`.
*   **`VoiceClient`**: Python client class managing PyAudio and WebSocket I/O.

## Common Issues & Fixes
*   **"AudioContext sample-rate mismatch"**: Fixed by allowing native browser sample rate and downsampling in JS.
*   **"GPU OOM"**: Reduce `model.size` in `app.yaml` or force `compute_type: int8`.
*   **"No audio detected"**: Check system microphone input volume or VAD threshold.

## Contribution Guidelines
See `CONTRIBUTING.md` for style guides and PR processes. We enforce `pylint` and `unittest`.
