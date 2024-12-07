from unittest.mock import MagicMock

import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))
block_size = 32

# Loop execution starts here
print("Loop is starting...") 

for ii in range(0, size, block_size):
    for jj in range(0, size, block_size):
        for kk in range(0, size, block_size):
            for i in range(ii, min(ii + block_size, size)):
                for j in range(jj, min(jj + block_size, size)):
                    for k in range(kk, min(kk + block_size, size)):
                        C[i][j] += A[i][k] * B[k][j]
            
print("Loop has finished.")  

