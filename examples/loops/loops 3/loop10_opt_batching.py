from unittest.mock import MagicMock

import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))
batch_size = 16  # Batch size for optimization

# Batching Optimization
print("Batching Loop is starting...")

# Loop through matrix blocks in batches
for i_batch_start in range(0, size, batch_size):
    i_batch_end = min(i_batch_start + batch_size, size)
    for j_batch_start in range(0, size, batch_size):
        j_batch_end = min(j_batch_start + batch_size, size)
        for k_batch_start in range(0, size, batch_size):
            k_batch_end = min(k_batch_start + batch_size, size)
            
            # Process each block of the matrix
            for i in range(i_batch_start, i_batch_end):
                for j in range(j_batch_start, j_batch_end):
                    for k in range(k_batch_start, k_batch_end):
                        C[i][j] += A[i][k] * B[k][j]

print("Batching Loop has finished.")
print(C)
