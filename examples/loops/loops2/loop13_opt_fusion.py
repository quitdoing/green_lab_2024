import numpy as np

size = 2000000
arr = np.random.rand(size)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
            
    return quicksort(left) + middle + quicksort(right)

print("Loop is starting...") 

sorted_arr = quicksort(arr)

print("Loop has finished.")
