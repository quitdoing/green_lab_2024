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

block_size = 64

print("Loop is starting...") 

num_rows = size

for j in range(0, num_rows, block_size):
    for b in range(block_size):
        if j + b < num_rows:
            sum_value = 0.0
            
            for k in range(rowstr[j + b], rowstr[j + b + 1]):
                sum_value += a[k] * p[colidx[k]]
            w[j + b] = sum_value

print("Loop has finished.")
