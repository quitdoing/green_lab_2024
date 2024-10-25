import numpy as np

size = 2000000 
arr = np.random.rand(size)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[(start + end) // 2]
        low, high = start, end
        
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
                
        if start < high:
            stack.append((start, high))
        if low < end:
            stack.append((low, end))
    
    return arr

print("Loop is starting...") 

sorted_arr = quicksort(arr)

print("Loop has finished.")

