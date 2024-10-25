import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))

print("Loop is starting...")

for i in range(0, size, 4):
    for j in range(0, size, 4):
        for k in range(size):
            
            for ii in range(4):
                for jj in range(4):
                    if (i + ii < size) and (j + jj < size):
                        C[i + ii][j + jj] += A[i + ii][k] * B[k][j + jj]

print("Loop has finished.")
