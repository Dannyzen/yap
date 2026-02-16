import socket
import sys
import subprocess
import time
from yap.config import Config

def ensure_daemon_running(host, port):
    """
    Checks if the daemon is running on the given host/port.
    If not, and auto_start is enabled in config, attempts to launch it.
    """
    try:
        with socket.create_connection((host, port), timeout=0.1):
            return True # Daemon IS running
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass # Daemon not running

    # Daemon not running, check config
    config = Config()
    if not config.get("daemon.auto_start", True):
        # Auto-start disabled
        # We return False because it is NOT running and we didn't start it
        return False

    # print(f"[INFO] Daemon not found on {host}:{port}. Auto-starting...", file=sys.stderr)
    
    cmd = config.get("daemon.command")
    if not cmd:
        # Default to running the module
        cmd = ["uv", "run", "yap-server"]

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
        # print("[INFO] Waiting for daemon to initialize...", file=sys.stderr)
        start_time = time.time()
        while time.time() - start_time < 20: # 20s timeout (model load can be slow)
            try:
                with socket.create_connection((host, port), timeout=0.1):
                    # print("[INFO] Daemon started successfully.", file=sys.stderr)
                    return True
            except (socket.timeout, ConnectionRefusedError, OSError):
                time.sleep(0.5)
            
        # print("[ERROR] Timeout waiting for daemon to start.", file=sys.stderr)
        return False
    except Exception as e:
        # print(f"[ERROR] Failed to auto-start daemon: {e}", file=sys.stderr)
        return False
