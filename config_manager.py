import yaml
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Lock

class ConfigHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
        self.last_modified = 0

    def on_modified(self, event):
        if event.src_path.endswith("app.yaml"):
            # De-bounce
            current_time = time.time()
            if current_time - self.last_modified > 1:
                self.last_modified = current_time
                self.callback()

class ConfigManager:
    def __init__(self, config_path="app.yaml"):
        self.config_path = os.path.abspath(config_path)
        self.config = {}
        self.lock = Lock()
        self.observers = []
        self._load_config()
        
        self.observer = Observer()
        event_handler = ConfigHandler(self._reload_config)
        self.observer.schedule(event_handler, path=os.path.dirname(self.config_path), recursive=False)
        self.observer.start()

    def _load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                new_config = yaml.safe_load(f)
            with self.lock:
                self.config = new_config
        except Exception as e:
            print(f"Error loading config: {e}")

    def _reload_config(self):
        print("Reloading config...")
        self._load_config()
        for callback in self.observers:
            callback(self.get_config())

    def get_config(self):
        with self.lock:
            return self.config.copy()

    def add_observer(self, callback):
        self.observers.append(callback)

    def stop(self):
        self.observer.stop()
        self.observer.join()
