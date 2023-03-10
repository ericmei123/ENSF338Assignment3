import requests
import json
import timeit
import matplotlib.pyplot as plt

def new_binary_search(arr, start, end, custom_p,  key, is_first =True):

    if start > end:
        return -1
    
    if is_first:
        mid = int((start+end)//custom_p)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return new_binary_search(arr, start, mid -1, 0, key, is_first = False)
        else:
            return new_binary_search(arr, mid+1, end, 0, key, is_first = False)
    else:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return new_binary_search(arr, start, mid -1, 0, key, is_first = False)
        else:
            return new_binary_search(arr, mid+1, end, 0, key, is_first = False)




url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json"
response = requests.get(url)
arr = json.loads(response.text)


taskurl = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json"
taskresponse = requests.get(taskurl)
tasks = json.loads(taskresponse.text)

ttlists = []

for i in tasks:
    ttlist = []
    k = timeit.timeit(lambda: new_binary_search(tasks, 0, len(tasks)-1, 1.7, i), number =1 )
    n = timeit.timeit(lambda: new_binary_search(tasks, 0, len(tasks)-1, 2.3, i), number =1 )
    h = timeit.timeit(lambda: new_binary_search(tasks, 0, len(tasks)-1, 8, i), number =1 )
    l = timeit.timeit(lambda: new_binary_search(tasks, 0, len(tasks)-1, 16, i), number =1 )
    ttlist.append(k)
    ttlist.append(n)
    ttlist.append(h)
    ttlist.append(l)
    min_index = ttlist.index(min(ttlist))
    ttlists.append(min_index)


tasks_num = []
j = 0
for i in tasks:
    tasks_num.append(i)
    j += 1


print(ttlists)
print(tasks_num)
nums = [0,1,2,3]

plt.scatter(ttlists,tasks_num)
plt.ylabel("Number Searched For")
plt.xticks(nums)

plt.xlabel("Custom Midpoint #")
plt.legend()
plt.show()