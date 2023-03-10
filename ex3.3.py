
import sys

def capacity(l: list): #getsizeof = 8 * capacity + 56
    return (sys.getsizeof(l) - 56) // 8

lst = []
prev_capacity = capacity(lst)
prev_capacity_btye = sys.getsizeof(lst)

for i in range(64):
    
    lst.append(i)
    new_capacity = capacity(lst)
    new_capacity_byte = sys.getsizeof(lst)

    if new_capacity != prev_capacity:
        print(f'Size of list in bytes changed from {prev_capacity_btye} to {new_capacity_byte},\nChanged at {len(lst)=}, new max {capacity(lst)=}\n') #gives list len versus capacity of list
        prev_capacity = new_capacity
        prev_capacity_btye = new_capacity_byte



