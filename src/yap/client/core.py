import asyncio
import json
import uuid
import sys
import numpy as np
import pyaudio
import websockets

from yap.config import Config
from .daemon import ensure_daemon_running


"""
Core client implementation for Yap.

This module provides the `VoiceClient` class which handles:
1.  Connecting to the server via WebSockets.
2.  Capturing audio from the microphone using PyAudio.
3.  Preprocessing audio (resampling, normalization).
4.  Sending audio data and receiving transcription results.
"""

class VoiceClient:
    """
    Client for capturing audio and streaming it to the Yap server.

    Handles audio capture via PyAudio, signal processing (resampling, normalization),
    and WebSocket communication.
    """
    def __init__(self, host="localhost", port=9090, auto_start=True):
        """
        Initialize the voice client.

        Args:
            host (str): The hostname of the server. Defaults to "localhost".
            port (int): The port of the server. Defaults to 9090.
            auto_start (bool): Whether to auto-start the server daemon. Defaults to True.
        """
        # Auto-start daemon if needed
        if auto_start:
            ensure_daemon_running(host, port)
        
        self.uri = f"ws://{host}:{port}"
        self.uid = str(uuid.uuid4())
        
        # Suppress ALSA/Jack error messages
        from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
        
        def py_error_handler(filename, line, function, err, fmt):
            pass
            
        ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
        c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
        
        try:
            asound = cdll.LoadLibrary('libasound.so')
            asound.snd_lib_error_set_handler(c_error_handler)
        except OSError:
            pass
            
        self.p = pyaudio.PyAudio()
        self.format = pyaudio.paInt16
        self.channels = 2 # Catch-all Stereo for Webcam compatibility
        self.rate = 32000 # High capture rate for Webcam
        self.chunk = 2048
        
        # Load Config
        self.config = Config()
        self.device_index = None
        
        # Intelligent Device Selection
        cfg_device = self.config.get("audio.input_device", "default")
        if isinstance(cfg_device, int):
             self.device_index = cfg_device

    async def run(self, duration=10, on_transcription=None, on_live_update=None, use_vad=True):
        """
        Connects to the server, streams audio, and handles incoming transcription updates.

        Args:
            duration (int): How long to record in seconds. Defaults to 10.
            on_transcription (callable, optional): Callback when final text is ready.
            on_live_update (callable, optional): Callback for real-time partial text updates.
            use_vad (bool): Whether to enable Voice Activity Detection on the server.
        """
        print(f"Connecting to {self.uri}...", file=sys.stderr)
        async with websockets.connect(self.uri) as websocket:
            # 1. Handshake
            handshake = {
                "uid": self.uid,
                "language": "en",
                "task": "transcribe",
                "model": "small",
                "use_vad": use_vad,
                "vad_parameters": {"threshold": 0.5} 
            }
            await websocket.send(json.dumps(handshake))
            
            # 2. Wait for Server Ready
            while True:
                resp = await websocket.recv()
                data = json.loads(resp)
                if data.get("message") == "SERVER_READY":
                    print(f"Server is ready! Recording for {duration} seconds...", file=sys.stderr)
                    break
            
            # 3. Stream & Receive
            stop_event = asyncio.Event()
            
            sender_task = asyncio.create_task(self.send_audio(websocket, stop_event))
            receiver_task = asyncio.create_task(self.receive_transcription(websocket, on_transcription, on_live_update))
            
            await asyncio.sleep(duration)
            stop_event.set()
            
            await sender_task
            await asyncio.sleep(1) # Flush
            await websocket.close()
            
            try:
                await receiver_task
            except websockets.exceptions.ConnectionClosed:
                pass

    async def send_audio(self, websocket, stop_event):
        """
        Captures audio from the microphone and streams it to the server.

        Includes a signal processing pipeline:
        1. Capture raw PCM (Int16, Stereo/Mono).
        2. Downmix to Mono.
        3. Resample to 16kHz (if needed).
        4. Normalize to Float32.
        5. Stream via WebSocket.

        Args:
            websocket: Active WebSocket connection.
            stop_event (asyncio.Event): Event to signal stopping the stream.
        """
        try:
            stream = self.p.open(
                format=self.format,
                channels=self.channels,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk,
                input_device_index=self.device_index
            )
        except OSError as e:
            print(f"[ERROR] Failed to open audio stream: {e}", file=sys.stderr)
            return

        try:
            while not stop_event.is_set():
                raw_data = stream.read(self.chunk, exception_on_overflow=False)
                
                # Conversion Pipeline:
                # 1. Stereo (2ch) -> Mono (1ch)
                # raw_data is int16 (2 bytes). 
                audio_array = np.frombuffer(raw_data, dtype=np.int16)
                
                if self.channels == 2:
                   # De-interleave and average: [L, R, L, R...] -> reshape to (N, 2)
                   audio_stereo = audio_array.reshape(-1, 2)
                   audio_mono = audio_stereo.mean(axis=1).astype(np.int16)
                else:
                   audio_mono = audio_array

                # 2. Downsample 32k -> 16k
                # Simple decimation [::2] works well for this factor
                if self.rate == 32000:
                     audio_resampled = audio_mono[::2]
                elif self.rate != 16000:
                     # For now, just pass through if 16k or unknown
                     audio_resampled = audio_mono
                else:
                     audio_resampled = audio_mono
                
                # 3. Convert Int16 -> Float32
                audio_np = audio_resampled.astype(np.float32) / 32768.0

                # Send
                await websocket.send(audio_np.tobytes())
                await asyncio.sleep(0.001)
        except Exception as e:
             print(f"\n[ERROR] Audio read loop failed: {e}", file=sys.stderr)
        finally:
            stream.stop_stream()
            stream.close()

    async def receive_transcription(self, websocket, callback=None, on_live_update=None):
        segments_map = {} 
        try:
            async for message in websocket:
                data = json.loads(message)
                if "segments" in data:
                    for seg in data["segments"]:
                        start_time = seg.get("start")
                        if start_time is not None:
                            segments_map[start_time] = seg["text"]
                    
                    # Update Live
                    if on_live_update:
                         # Compute current text
                        current_text = self._compile_text(segments_map)
                        on_live_update(current_text)

        except Exception:
            pass
        finally:
            final_text = self._compile_text(segments_map)
            if callback:
                callback(final_text)

    def _compile_text(self, segments_map):
        sorted_keys = sorted(segments_map.keys(), key=float)
        sorted_segments = [segments_map[k] for k in sorted_keys]
        
        # De-duplicate identical consecutive segments
        unique_segments = []
        if sorted_segments:
            unique_segments.append(sorted_segments[0])
            for seg in sorted_segments[1:]:
                if seg.strip() != unique_segments[-1].strip():
                    unique_segments.append(seg)
        
        return " ".join(unique_segments).strip()
