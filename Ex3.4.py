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
            # self.tail points last element, self.head points first, so if tail+1 = size, queue maxed out
            if (self.tail + 1) % self.size == self.head:
                self.unlock()
                # Wait for one second and try again
                time.sleep(1)
            else:
                # Insert the element and update the tail pointer
                if self.head == -1:
                    self.head = 0
                # makes sure that it stays a circular queue by ensuring tail+1 is next position
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                return

    def dequeue(self):
        while True:
            self.lock()
            if self.head == self.tail:
                # Queue is empty
                data = None
                self.unlock()
                # Wait for one second and try again
                time.sleep(1)
            else:
                self.head = (self.head + 1) % self.size
                data = self.queue[self.head]
                self.unlock()
                time.sleep(1)
                return data


def producer():
    while True:
        randint = random.randint(1, 10)
        time.sleep(randint)
        q.enqueue(randint)


def consumer():
    consumerrandint = random.randint(1, 10)
    while True:
        time.sleep(consumerrandint)
        data = q.dequeue()
        if data != None:
            print(f"Consumed number: {data}")


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
