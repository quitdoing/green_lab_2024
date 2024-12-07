from unittest.mock import MagicMock

import numpy as np

size = 200

A = np.random.rand(size, size)
B = np.random.rand(size, size)

C = np.zeros((size, size))

# Loop execution starts here
print("Loop is starting...") 


for i in range(0, size, 4):
    for j in range(0, size, 4):
        for k in range(size):
            C[i + 0][j + 0] += A[i + 0][k] * B[k][j + 0];
            C[i + 0][j + 1] += A[i + 0][k] * B[k][j + 1];
            C[i + 0][j + 2] += A[i + 0][k] * B[k][j + 2];
            C[i + 0][j + 3] += A[i + 0][k] * B[k][j + 3];

            C[i + 1][j + 0] += A[i + 1][k] * B[k][j + 0];
            C[i + 1][j + 1] += A[i + 1][k] * B[k][j + 1];
            C[i + 1][j + 2] += A[i + 1][k] * B[k][j + 2];
            C[i + 1][j + 3] += A[i + 1][k] * B[k][j + 3];

            C[i + 2][j + 0] += A[i + 2][k] * B[k][j + 0];
            C[i + 2][j + 1] += A[i + 2][k] * B[k][j + 1];
            C[i + 2][j + 2] += A[i + 2][k] * B[k][j + 2];
            C[i + 2][j + 3] += A[i + 2][k] * B[k][j + 3];


            C[i + 3][j + 0] += A[i + 3][k] * B[k][j + 0];
            C[i + 3][j + 1] += A[i + 3][k] * B[k][j + 1];
            C[i + 3][j + 2] += A[i + 3][k] * B[k][j + 2];
            C[i + 3][j + 3] += A[i + 3][k] * B[k][j + 3];
            
print("Loop has finished.")  

