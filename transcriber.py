from faster_whisper import WhisperModel

class Transcriber:
    """Wrapper for Faster Whisper model inference."""

    def __init__(self, model_size="tiny", device="cpu", compute_type="int8"):
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        print(f"Loading Whisper model: {model_size} on {device}...")
        try:
            self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def transcribe(self, audio_data):
        """
        Transcribes audio data to text.
        
        Args:
            audio_data: Float32 numpy array of audio samples.
        """
        if self.model is None:
            return "Model not loaded."
        
        segments, info = self.model.transcribe(audio_data, beam_size=1)
        text = ""
        for segment in segments:
            text += segment.text
        return text

    def update_config(self, model_size=None, device=None, compute_type=None):
        """Updates model configuration and reloads if necessary."""
        if model_size != self.model_size or device != self.device or compute_type != self.compute_type:
            self.model_size = model_size or self.model_size
            self.device = device or self.device
            self.compute_type = compute_type or self.compute_type
            # Reload model
            try:
                self.model = WhisperModel(self.model_size, device=self.device, compute_type=self.compute_type)
            except Exception as e:
                print(f"Error reloading model: {e}")
