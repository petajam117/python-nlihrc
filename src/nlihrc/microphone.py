import queue
import sys
import sounddevice

class MicReceiver():
    def __init__(self, buffersize):
        self.q = queue.Queue()
        self.close_thread = False
        self.rate = 16000
        self.buffersize = buffersize
        self.audiostream = sounddevice.RawInputStream(samplerate=self.rate, 
                                    blocksize=self.buffersize, 
                                    device=None, 
                                    dtype='int16', 
                                    channels=1, 
                                    callback=self.callback)

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))
    
    def start(self):
        self.audiostream.start()
    
    def stop(self):
        self.audiostream.stop()
