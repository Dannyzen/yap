# Fast Voice-to-Text

A high-performance, local voice-to-text system using `faster-whisper`. Designed for **low latency** and **hardware flexibility**.

## Features
- **Split Architecture**: Client/Server design decoupled via WebSockets. Run the heavy inference server on a powerful machine (or background process) and the lightweight client anywhere.
- **Auto-Daemon**: The client automatically starts the server in the background if it's not running. No need to manually manage processes.
- **Hardware Optimized**:
    - **Intelligent Device Selection**: Auto-detects preferred input devices (e.g., C920 Webcam) specified in config.
    - **ALSA Error Suppression**: Clean console output by suppressing noisy low-level audio driver errors.
- **Production Ready**: Integrated Voice Activity Detection (VAD) to filter silence, robust error handling, and reconnection logic.
- **Hot-Reload Config**: Edit `app.yaml` and changes (like model size or input device) apply instantly without restarting.

## Installation
```bash
# Install dependencies and package in editable mode
uv pip install -e .
```

## Usage

### 1. Running the Example (Easiest)
Run the "Cowsay" example to see it in action:
```bash
uv run examples/cowsay_app.py
```
This will:
1.  **Auto-start** the `fast-voice-server` daemon if needed.
2.  Record audio for 10 seconds.
3.  Display the transcript spoken by a cow.

### 2. Visual Client (Recommended)
For a premium terminal experience with live scrolling and status indicators:
```bash
uv run fast-voice-client
```

### 3. Browser Monitor
View your transcripts in real-time on any device (phone, tablet, laptop) by opening the monitor page.

1.  **Open the Monitor**:
    Open `src/fast_voice/server/static/index.html` in your browser.
2.  **Connect**:
    Click the **Connect** button.
3.  **Speak**:
    Run any client (e.g., `uv run examples/cowsay_app.py`) and start talking. The words will appear instantly in the browser.

### 4. Manual Server (Optional)
If you prefer to run the server manually (e.g., for debugging logs):
```bash
uv run fast-voice-server
```

### 5. Using the Client API
Build your own voice-controlled apps easily:
```python
import asyncio
from fast_voice.client.core import VoiceClient

async def main():
    client = VoiceClient()
    
    # Callback for when text is finalized
    def on_transcribed(text):
        print(f"You said: {text}")

    # Run for 10 seconds (or indefinitely with a loop/event)
    await client.run(duration=10, on_transcription=on_transcribed)

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration
Edit `app.yaml` to configure the system. key settings include:

- **Audio Input**: Select specific device index or use "default".
- **Model**: Choose `tiny`, `small`, `medium`, or `large-v3`.
- **Compute**: Use `int8` (CPU friendly) or `float16` (GPU).
- **VAD**: Enable/Disable Voice Activity Detection.

## Architecture
The system consists of two main components:
1.  **Client (`src/fast_voice/client`)**: Lightweight. Captures audio using `PyAudio`, handles device selection, downsampling, and streams raw PCM to the server via WebSockets.
2.  **Server (`src/fast_voice/server`)**: Heavy. Runs `faster-whisper` model. Accepts audio streams, performs VAD, and executes inference.

## Testing
The project includes a robust testing SDK for headless environments.

### Automated E2E Test
Verifies the full pipeline (Client -> Network -> Server -> Whisper) without a microphone.
```bash
uv run python -m unittest tests/test_e2e.py
```

### Simulation Client
Use the simulation client to test with synthetic audio or WAV files:
```python
from fast_voice.testing import SimulationClient

# 1. Use built-in synthetic voice
client = SimulationClient()

# 2. Or stream a custom WAV file
# client = SimulationClient(audio_file="speech.wav")

await client.run(duration=5)
```

## Development
```bash
# Run Unit Tests
uv run python -m unittest tests/test_client.py
```
