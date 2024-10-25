import numpy as np

size = 2000000
arr = np.random.rand(size)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print("Loop is starting...") 

sorted_arr = quicksort(arr)

print("Loop has finished.")
