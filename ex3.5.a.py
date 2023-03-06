
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def search_array_inefficient(arr, target): #go throughs the whole array to search for target
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def search_array_efficient(arr, target): #binary search
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

n = 1000
arr = np.arange(1, 1001)
target = arr[random.randint(0,n-1)]

inefficient_times = []
efficient_times = []

num_measurements = 100

for i in range(num_measurements):
    start = time.time()
    search_array_inefficient(arr, target)
    end = time.time()
    inefficient_times.append(end-start)

for i in range(num_measurements):
    start = time.time()
    search_array_efficient(arr, target)
    end = time.time()
    efficient_times.append(end-start)

x = range(num_measurements)
plt.scatter(x, inefficient_times, label='Inefficient')
plt.scatter(x, efficient_times, label='Efficient')
plt.legend()
plt.show()

print(f"Inefficient average time: {sum(inefficient_times)/num_measurements:.8f}")
print(f"Efficient average time: {sum(efficient_times)/num_measurements:.8f}")
