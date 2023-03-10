import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListPQ:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            if data > self.head.data:
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next is not None and current.next.data > data:
                    current = current.next
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

    def extract(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self._heapify()

    def _heapify(self):
        for i in range(self.size//2, -1, -1):
            self._sift_down(i)

    def _sift_down(self, i):
        while 2*i+1 < self.size:
            left = 2*i+1
            right = 2*i+2
            j = left
            if right < self.size and self.arr[right] > self.arr[left]:
                j = right
            if self.arr[i] >= self.arr[j]:
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i = j

    def insert(self, x):
        self.arr.append(x)
        self.size += 1
        self._sift_up(self.size-1)

    def _sift_up(self, i):
        while i > 0 and self.arr[(i-1)//2] < self.arr[i]:
            self.arr[(i-1)//2], self.arr[i] = self.arr[i], self.arr[(i-1)//2]
            i = (i-1)//2

    def extract(self):
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self._sift_down(0)
        return self.arr.pop()

class HeapPQ:
    def __init__(self):
        self.heap = Heap([])

    def enqueue(self, data):
        self.heap.insert(data)

    def extract(self):
        return self.heap.extract()



insertions = [random.randint(0, 1200) for _ in range(1200)]
epq = HeapPQ()
ipq = ListPQ()
def testefficientpq(epq):
    for x in insertions:
        epq.enqueue(x)
    for j in insertions:
        (epq.extract())


def testinefficientpq(ipq):
    for x in insertions:
        ipq.enqueue(x)
    for j in insertions:
        (ipq.extract())
    

heaptime  = timeit.repeat("testefficientpq(epq)", setup="epq = HeapPQ()", globals={"HeapPQ":HeapPQ, "testefficientpq":testefficientpq}, repeat=125, number=1)
inefficienttime = timeit.repeat("testinefficientpq(ipq)", setup="ipq = ListPQ()", globals={"ListPQ":ListPQ, "testinefficientpq":testinefficientpq}, repeat=125, number=1)


print("The minimum time for the efficient priority queue implementation was " + str(min(heaptime)) + "seconds")
print("The minimum time for the inefficient priority queue implementation was " + str(min(inefficienttime)) + "seconds")
measurement_number =[]
for i in range(125):
    measurement_number.append(i)

plt.scatter(measurement_number,heaptime, label ="Efficient Priority Queue")
plt.scatter(measurement_number,inefficienttime, label = "Inefficient Priority Queue")
plt.legend(loc="upper right")

plt.ylabel("Measured time")
plt.xlabel("Measurement number")
plt.show()
