import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/System-01/Downloads"

class FileMovementHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(event.src_path+"This file is being modified")


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


while True:
    time.sleep(2)
    print("running...")
