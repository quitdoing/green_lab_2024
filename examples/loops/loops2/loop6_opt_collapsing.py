import numpy as np

M = 2000
N = 2000

cost = np.random.rand(N + 1, M + 1)
x = np.random.rand(N + 1, M + 1)
trace = np.zeros((N + 1, M + 1), dtype=int)

print("Loop is starting...") 
for idx in range(1, (M + 1) * (N + 1)):
    j = idx // (N + 1)
    i = idx % (N + 1)
    if j > M or i > N:
        continue
    c0 = cost[i - 1][j - 1]
    c1 = cost[i - 1][j]
    c2 = cost[i][j - 1]
    if c0 < c1 and c0 < c2:
        c, t = c0, 0
    elif c1 < c0 and c1 < c2:
        c, t = c1, 1
    else:
        c, t = c2, 2
    cost[i][j] = x[i - 1][j - 1] + c
    trace[i][j] = t

print("Loop has finished.")  