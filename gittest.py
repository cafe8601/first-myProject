from threading import Thread
import threading

class Cultery:
    # knives = attrib(default = 0)
    # forks = attrib(default = 0)
    
    def __init__(self, knives, forks):
        self.knives = knives
        self.forks = forks
        self.lock = threading.Lock()
    
    def give(self, to: 'Cultery', knives = 0, forks = 0):
        self.change(-knives, -forks)
        to.change(knives, forks)
        
    def change(self, knives, forks):
        # with self.lock:
        self.lock.acquire()
        self.knives += knives
        self.forks += forks
        self.lock.release()
        
if __name__ == "__main__":
    a = Cultery(15, 18)
    a.change(5, 10)
    print(f"{a.knives} , {a.forks}") 