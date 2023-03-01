import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            # Check if the queue is full
            if (self.tail + 1) % self.size == self.head: #self.tail points last element, self.head points first, so if tail+1 = size, queue maxed out
                self.unlock() 
                # Wait for one second and try again
                time.sleep(1)
            else:
                # Insert the element and update the tail pointer
                if self.head == -1:
                    self.head = 0
                self.tail = (self.tail + 1) % self.size #makes sure that it stays a circular queue by ensuring tail+1 is next position
                self.queue[self.tail] = data
                self.unlock()
                return
    
    def dequeue(self):
        # Implement dequeue function
        pass


def producer():
    while True:
        num = random.randint(1, 10)
        time.sleep(num)
        q.enqueue(num)



def consumer():
    while True:
        # Implement consumer function
        pass

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()