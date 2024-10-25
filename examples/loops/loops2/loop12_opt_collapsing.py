import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))

print("Loop is starting...")

for idx in range(size * size * size):
    i = idx // (size * size)
    j = (idx // size) % size
    k = idx % size
    C[i][j] += A[i][k] * B[k][j]

print("Loop has finished.")
