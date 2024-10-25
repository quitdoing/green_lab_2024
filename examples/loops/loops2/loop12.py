from unittest.mock import MagicMock

import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))

print("Loop is starting...")

for i in range(size):
    for j in range(size):
        for k in range(size):
            C[i][j] += A[i][k] * B[k][j]

print("Loop has finished.")


