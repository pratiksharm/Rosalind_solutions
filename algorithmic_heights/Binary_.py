import time
from timeit import default_timer as timer

##return the index of the array if present else return -1
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,low, mid -1, x)
        
        else:
            return binary_search(arr, mid + 1, high, x)
    
    else:
        return -1

arr = [ 2, 3,4, 5, 10, 40]

x = 10
start = time.time()
result = binary_search(arr, 0, len(arr) -1, x)

if result != -1:
    print('The Element is present at index ', str(result))
else:
    print('Element is absent in the given array')

end = time.time()
print(end-start)
