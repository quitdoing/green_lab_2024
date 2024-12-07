import numpy as np


size = 150
nx0, ny0, nz0 = size, size, size

v = np.random.rand(5, nx0, ny0, nz0)

sum_norm = [0] * 5

print("Loop is starting...")

for k in range(2, nz0 - 1):
    for j in range(ny0):
        for i in range(nx0):
            for m in range(5):
                sum_norm[m] += v[m, i, j, k] ** 2

print("Loop has finished.")

