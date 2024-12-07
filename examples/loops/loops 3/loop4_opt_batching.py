import numpy as np

M = 2000
N = 2000

cost = np.random.rand(N + 1, M + 1)
x = np.random.rand(N + 1, M + 1)
trace = np.zeros((N + 1, M + 1), dtype=int)

# Batching Optimization
print("Batching Loop is starting...")

batch_size = 16  # Process 16 rows at a time

for j in range(1, M + 1):  # Loop over columns
    for i_batch_start in range(1, N + 1, batch_size):  # Batch rows
        i_batch_end = min(i_batch_start + batch_size, N + 1)
        
        for i in range(i_batch_start, i_batch_end):  # Process rows in the batch
            c0 = cost[i - 1, j - 1]
            c1 = cost[i - 1, j]
            c2 = cost[i, j - 1]
            if c0 < c1 and c0 < c2:
                c, t = c0, 0
            elif c1 < c0 and c1 < c2:
                c, t = c1, 1
            else:
                c, t = c2, 2
            cost[i, j] = x[i - 1, j - 1] + c
            trace[i, j] = t

print("Batching Loop has finished.")
