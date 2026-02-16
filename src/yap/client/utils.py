import sys
import json
import socket
import subprocess
import time
import os
from yap.config import Config
from yap.whisper_live.client import TranscriptionClient, Client

def ensure_daemon_running(host, port):
    """
    Checks if the daemon is running on the given host/port.
    If not, and auto_start is enabled in config, attempts to launch it.
    """
    try:
        with socket.create_connection((host, port), timeout=1):
            return # Daemon is running
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass # Daemon not running

    # Daemon not running, check config
    config = Config()
    if not config.get("daemon.auto_start", True):
        return # Auto-start disabled or not configured

    print(f"[INFO] Daemon not found on {host}:{port}. Auto-starting...", file=sys.stderr)
    
    cmd = config.get("daemon.command")
    if not cmd:
        # Infer path to v2td.py relative to this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        v2td_path = os.path.join(base_dir, "v2td.py")
        # Assume 'uv' is in path, or just run with same python executable if possible
        # Using 'uv run' as standard for this project
        cmd = ["uv", "run", v2td_path]

    try:
        # Launch independent subprocess
        # stdout/stderr to DEVNULL to avoid cluttering client
        subprocess.Popen(
            cmd,
            start_new_session=True, # Detach so it survives client exit
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Wait for port to open
        print("[INFO] Waiting for daemon to initialize...", file=sys.stderr)
        start_time = time.time()
        while time.time() - start_time < 20: # 20s timeout (model load can be slow)
            try:
                with socket.create_connection((host, port), timeout=1):
                    print("[INFO] Daemon started successfully.", file=sys.stderr)
                    return
            except (socket.timeout, ConnectionRefusedError, OSError):
                time.sleep(0.5)
            
        print("[ERROR] Timeout waiting for daemon to start.", file=sys.stderr)
    except Exception as e:
        print(f"[ERROR] Failed to auto-start daemon: {e}", file=sys.stderr)


# Subclass Client to inject initial_prompt
class ContextClient(Client):
    def __init__(self, *args, initial_prompt=None, **kwargs):
        self.initial_prompt = initial_prompt
        super().__init__(*args, **kwargs)

    def on_open(self, ws):
        # We write to stderr to avoid polluting stdout which might be piped
        # But for UI client (main.py), stderr usage is fine or we can silence it.
        # Check if we are in main script? No, library code should be generic.
        # We can add a logging callback or just use sys.stderr.
        # print("[INFO]: Opened connection", file=sys.stderr) 
        
        ws.send(
            json.dumps(
                {
                    "uid": self.uid,
                    "language": self.language,
                    "task": self.task,
                    "model": self.model,
                    "use_vad": self.use_vad,
                    "send_last_n_segments": self.send_last_n_segments,
                    "no_speech_thresh": self.no_speech_thresh,
                    "clip_audio": self.clip_audio,
                    "same_output_threshold": self.same_output_threshold,
                    "enable_translation": self.enable_translation,
                    "target_language": self.target_language,
                    "initial_prompt": self.initial_prompt
                }
            )
        )

# Custom TranscriptionClient that uses ContextClient
class ContextTranscriptionClient(TranscriptionClient):
    def __init__(
        self,
        host,
        port,
        lang=None,
        translate=False,
        model="small",
        use_vad=True,
        use_wss=False,
        save_output_recording=False,
        output_recording_filename="./output_recording.wav",
        output_transcription_path="./output.srt",
        log_transcription=True,
        mute_audio_playback=False,
        send_last_n_segments=10,
        no_speech_thresh=0.45,
        clip_audio=False,
        same_output_threshold=10,
        transcription_callback=None,
        enable_translation=False,
        target_language="fr",
        translation_callback=None,
        translation_srt_file_path="./output_translated.srt",
        enable_timestamps=False,
        input_device_index=None,
        initial_prompt=None
    ):
        # Auto-start check
        ensure_daemon_running(host, port)
        
        self.client = ContextClient(
            host,
            port,
            lang,
            translate,
            model,
            srt_file_path=output_transcription_path,
            use_vad=use_vad,
            use_wss=use_wss,
            log_transcription=log_transcription,
            send_last_n_segments=send_last_n_segments,
            no_speech_thresh=no_speech_thresh,
            clip_audio=clip_audio,
            same_output_threshold=same_output_threshold,
            transcription_callback=transcription_callback,
            enable_translation=enable_translation,
            target_language=target_language,
            translation_callback=translation_callback,
            translation_srt_file_path=translation_srt_file_path,
            enable_timestamps=enable_timestamps,
            initial_prompt=initial_prompt
        )
        
        # Init Tee
        from yap.whisper_live.client import TranscriptionTeeClient
        TranscriptionTeeClient.__init__(
            self,
            [self.client],
            save_output_recording=save_output_recording,
            output_recording_filename=output_recording_filename,
            mute_audio_playback=mute_audio_playback,
            input_device_index=input_device_index
        )
