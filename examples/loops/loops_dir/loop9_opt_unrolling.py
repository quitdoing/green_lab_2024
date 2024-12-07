import numpy as np
from scipy.sparse import random as sparse_random


size = 5000
density = 0.3


sparse_matrix = sparse_random(size, size, density=density, format='csc', dtype=float)


a = sparse_matrix.data 
rowstr = sparse_matrix.indptr
colidx = sparse_matrix.indices


p = np.random.rand(size)


w = np.zeros(size)

num_rows = size
# Unrolling Optimization
print("Unrolling Loop is starting...")

for j in range(num_rows):
    sum_value = 0.0  
    k_start = rowstr[j]
    k_end = rowstr[j + 1]
    
    # Unrolling inner loop
    for k in range(k_start, k_end - 3, 4):  # Process 4 elements at a time
        sum_value += (
            a[k] * p[colidx[k]] +
            a[k + 1] * p[colidx[k + 1]] +
            a[k + 2] * p[colidx[k + 2]] +
            a[k + 3] * p[colidx[k + 3]]
        )
    
    # Handle remaining elements (if not a multiple of 4)
    for k in range(k_end - (k_end - k_start) % 4, k_end):
        sum_value += a[k] * p[colidx[k]]
    
    w[j] = sum_value

print("Unrolling Loop has finished.")
