import yaml
import time
import threading
import os
import logging
from typing import Any, Dict, Callable, List

class Config:
    _instance = None
    _lock = threading.Lock()
    _callbacks: List[Callable[[Dict], None]] = []
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Config, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self, config_path: str = "app.yaml"):
        if self._initialized:
            return
        
        self.config_path = config_path
        self._data = {}
        self._last_mtime = 0
        self._stop_event = threading.Event()
        self._logger = logging.getLogger("Config")
        
        # Initial load and start watcher
        self.reload()
        
        # Start watcher thread
        self._watcher_thread = threading.Thread(target=self._watch_loop, daemon=True)
        self._watcher_thread.start()
        
        self._initialized = True

    def _load_yaml(self) -> Dict:
        try:
            # Search for config in current and parent directories
            search_paths = [
                self.config_path,
                os.path.join(os.path.dirname(__file__), "../../" + self.config_path),
                os.path.join(os.getcwd(), "../" + self.config_path),
                "../app.yaml"
            ]
            
            found_path = None
            for p in search_paths:
                if os.path.exists(p):
                    found_path = p
                    break
            
            if not found_path:
                self._logger.warning(f"Config file not found in search paths: {search_paths}. Using defaults.")
                return {}
            
            # Update path to the found one so watcher works
            self.config_path = found_path
                
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            self._logger.error(f"Error loading config: {e}")
            return self._data # Return old data on failure

    def reload(self):
        new_data = self._load_yaml()
        if new_data != self._data:
            self._data = new_data
            self._last_mtime = os.path.exists(self.config_path) and os.path.getmtime(self.config_path) or 0
            self._notify_listeners()
            self._logger.info(f"Config reloaded from {self.config_path}")

    def _watch_loop(self):
        """Monitor config file for changes."""
        while not self._stop_event.is_set():
            time.sleep(2)
            try:
                if os.path.exists(self.config_path):
                    mtime = os.path.getmtime(self.config_path)
                    if mtime > self._last_mtime:
                        self.reload()
            except Exception as e:
                self._logger.error(f"Error in config watcher: {e}")

    def register_callback(self, callback: Callable[[Dict], None]):
        """Register a function to be called when config changes."""
        self._callbacks.append(callback)

    def _notify_listeners(self):
        for callback in self._callbacks:
            try:
                callback(self._data)
            except Exception as e:
                self._logger.error(f"Error in config callback: {e}")

    def get(self, path: str, default: Any = None) -> Any:
        """
        Get a value using dot notation, e.g. "model.size"
        """
        keys = path.split('.')
        value = self._data
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default
        return value if value is not None else default

    @property
    def data(self):
        return self._data
