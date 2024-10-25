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

print("Loop is starting...") 

for j in range(num_rows):
    sum_value = 0.0
    end = rowstr[j + 1]
    for k in range(rowstr[j], end):
        sum_value += a[k] * p[colidx[k]]
    w[j] = sum_value

print("Loop has finished.")
