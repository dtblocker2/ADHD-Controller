import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import sys
import platform

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None
        self.python_executable = self.get_virtualenv_python()
        self.start_app()

    def get_virtualenv_python(self):
        # Adjust this if your venv is in a different directory
        venv_dir = "venv"
        if platform.system() == "Windows":
            return os.path.join(venv_dir, "Scripts", "python.exe")
        else:
            return os.path.join(venv_dir, "bin", "python")

    def start_app(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([self.python_executable, self.script_path])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Detected change in {event.src_path}, restarting app...")
            self.start_app()

if __name__ == "__main__":
    path_to_watch = "."  # Watch current directory
    script_to_run = "main.py"  # Your PyQt main script

    event_handler = RestartHandler(script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.process.kill()
    observer.join()
