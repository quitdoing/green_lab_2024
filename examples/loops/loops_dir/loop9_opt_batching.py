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

# Loop execution starts here
print("Batching Loop is starting...")

batch_size = 4  # Number of rows to process per batch
temp_batch_sums = [0.0] * batch_size  # Temporary accumulators for a batch of rows

for j_batch_start in range(0, num_rows, batch_size):
    j_batch_end = min(j_batch_start + batch_size, num_rows)  # Define batch range
    temp_batch_sums = [0.0] * (j_batch_end - j_batch_start)  # Reset batch accumulators

    # Process the rows in the current batch
    for j in range(j_batch_start, j_batch_end):
        sum_value = 0.0
        for k in range(rowstr[j], rowstr[j + 1]):  # Iterate through non-zero entries
            sum_value += a[k] * p[colidx[k]]
        temp_batch_sums[j - j_batch_start] = sum_value  # Store sum for this row in the batch

    # Update w for all rows in the batch
    for idx, j in enumerate(range(j_batch_start, j_batch_end)):
        w[j] = temp_batch_sums[idx]  # Assign accumulated sum to w

print("Batching Loop has finished.")
