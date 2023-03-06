
import sys

lst = []
prev_capacity = 0

# Loop over integers from 0 to 63 and add them to the list
for i in range(64):
    lst.append(i)
    
    # Get the size of the list in bytes
    size = sys.getsizeof(lst)
    
    # Calculate the capacity of the list
    capacity = size // sys.getsizeof(lst[0])
    # Check if the capacity has changed and print a message if it has
    if capacity != prev_capacity:
        print(f"Capacity changed to {capacity} at length {len(lst)}")
        prev_capacity = capacity