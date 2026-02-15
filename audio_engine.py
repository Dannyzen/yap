import sounddevice as sd
import queue

class AudioEngine:
    """Handles audio input streaming."""
    
    def __init__(self, sample_rate=16000, channels=1, device_index=None):
        self.sample_rate = sample_rate
        self.channels = channels
        self.device_index = device_index
        self.queue = queue.Queue()
        self.running = False
        self.stream = None

    def start(self):
        """Starts the audio stream."""
        self.running = True
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            device=self.device_index,
            callback=self._audio_callback,
            dtype="float32"
        )
        self.stream.start()

    def _audio_callback(self, indata, frames, time, status):
        """Callback for processing audio frames."""
        if status:
            print(status)
        if self.running:
            self.queue.put(indata.copy())

    def get_audio_chunk(self):
        """Retrieves the next available audio chunk."""
        try:
            return self.queue.get(timeout=0.1)
        except queue.Empty:
            return None

    def stop(self):
        """Stops the audio stream."""
        self.running = False
        if self.stream:
            self.stream.stop()
            self.stream.close()

    def update_config(self, sample_rate=None, device_index=None):
        """Updates configuration and restarts stream if necessary."""
        restart = False
        if self.running:
            self.stop()
            restart = True
        
        if sample_rate:
            self.sample_rate = sample_rate
        if device_index is not None:
            self.device_index = device_index

        if restart:
            self.start()
