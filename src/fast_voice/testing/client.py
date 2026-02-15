import asyncio
import numpy as np
# import audioop - Deprecated
import sys
import os
import wave
from fast_voice.client.core import VoiceClient

class SimulationClient(VoiceClient):
    """
    A headless client for testing the voice pipeline.
    
    Modes:
    1. File Mode: Streams a WAV file if provided and exists.
    2. Synthetic Mode: Generates a harmonic "robot voice" (sawtooth-like) 
       that triggers VAD without needing external files.
    """
    def __init__(self, host="localhost", port=9090, audio_file=None):
        super().__init__(host, port)
        self.audio_file = audio_file
        self.phase = 0.0

    async def send_audio(self, websocket, stop_event):
        """
        Overrides VoiceClient.send_audio to stream simulation data.
        """
        if self.audio_file and os.path.exists(self.audio_file):
            await self._stream_file(websocket, stop_event)
        else:
            await self._stream_synthetic(websocket, stop_event)

    async def _stream_file(self, websocket, stop_event):
        print(f"[SIMULATION] Stream Mode: File ({self.audio_file})")
        try:
            with wave.open(self.audio_file, 'rb') as wf:
                channels = wf.getnchannels()
                width = wf.getsampwidth()
                rate = wf.getframerate()
                target_rate = 16000
                
                while not stop_event.is_set():
                    frames_to_read = int(rate * 0.1) # 100ms chunks
                    data = wf.readframes(frames_to_read)
                    if not data:
                        wf.rewind()
                        data = wf.readframes(frames_to_read)
                    
                    # Convert to standard pipeline format
                    audio_array = np.frombuffer(data, dtype=np.int16)

                    if channels == 2:
                        audio_stereo = audio_array.reshape(-1, 2)
                        audio_mono = audio_stereo.mean(axis=1).astype(np.int16)
                    else:
                        audio_mono = audio_array
                    
                    if rate != target_rate:
                        # Linear interpolation resampling
                        full_len = len(audio_mono)
                        target_len = int(full_len * target_rate / rate)
                        audio_resampled = np.interp(
                            np.linspace(0, full_len, target_len, endpoint=False),
                            np.arange(full_len),
                            audio_mono
                        ).astype(np.int16)
                    else:
                        audio_resampled = audio_mono
                    
                    audio_np = audio_resampled.astype(np.float32) / 32768.0
                    await websocket.send(audio_np.tobytes())
                    
                    duration = len(data) / width / rate # Approx
                    await asyncio.sleep(0.09) # Slightly faster than realtime to prevent buffer underrun
        except Exception as e:
            print(f"[ERROR] File stream failed: {e}", file=sys.stderr)

    async def _stream_synthetic(self, websocket, stop_event):
        print("[SIMULATION] Stream Mode: Synthetic (Advanced Vowel)")
        rate = 16000
        chunk_size = 1600 # 100ms
        
        # Human Vowel Parameters ('Ah')
        f0 = 140.0 # Fundamental (Male)
        phase = 0.0
        
        while not stop_event.is_set():
            t = (np.arange(chunk_size) + phase) / rate
            phase += chunk_size
            
            # 1. Base Glottal Source (Pulse Train / Sawtooth-ish)
            # Rich in harmonics (1/n)
            source = np.zeros_like(t)
            for k in range(1, 20): # 20 harmonics
                source += (1.0/k) * np.sin(2 * np.pi * (f0 * k) * t)
            
            # 2. Add Vibrato (5Hz freq modulation)
            # Simplified: just AM modulation for now
            vibrato = 1.0 + 0.1 * np.sin(2 * np.pi * 5.0 * t)
            source *= vibrato
            
            # 3. Burst Envelope (Talk 2s, Silence 1s)
            time_in_cycle = (phase / rate) % 3.0
            if time_in_cycle > 2.0:
                source *= 0.001 # Silence floor
            
            # 4. Amplitude Normalization
            source = np.clip(source, -1.0, 1.0)
            
            audio_np = source.astype(np.float32)
            await websocket.send(audio_np.tobytes())
            
            await asyncio.sleep(0.1)
