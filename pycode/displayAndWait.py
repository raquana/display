import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileModifiedEvent, FileCreatedEvent
import sys
import logging


class PFW(FileSystemEventHandler):
    def __init__(self):
        self.theProc = subprocess.Popen(['../rpi-rgb-led-matrix/led-matrix','1','test.ppm'],
                                        stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
#        print 'Process Id: ' + str(self.theProc.pid)
        self.running = True
        self.fullStop = False

    def isRunning(self):
        return self.running

    def isFullStop(self):
        return self.fullStop

    def stopRunning(self):
        self.running = False
#        print 'Stopping process'
#        print self.theProc.communicate(input=" ")[0]
        self.theProc.communicate(input=" ")[0]
#        print 'Stopped'

    def on_modified(self, event):
	if self.running and isinstance(event, FileModifiedEvent) and event.src_path == './test.ppm':
            self.stopRunning()

    def on_created(self, event):
        if self.running and isinstance(event, FileCreatedEvent)  and event.src_path == './stop':
            self.fullStop = True
            self.stopRunning()


try:

    while True:
        meh = PFW()
        observer = Observer()
        observer.schedule(meh, '.')
        observer.start()
        while meh.isRunning():
            time.sleep(1)
        observer.stop()
        observer.join()
        if meh.isFullStop():
            break

except KeyboardInterrupt:
    print 'FORCED STOP - Display may not be clear'
