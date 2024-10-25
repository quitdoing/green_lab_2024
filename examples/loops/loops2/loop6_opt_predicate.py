import numpy as np

M = 2000
N = 2000

cost = np.random.rand(N + 1, M + 1)
x = np.random.rand(N + 1, M + 1)
trace = np.zeros((N + 1, M + 1), dtype=int)

print("Loop is starting...") 
for j in range(1, M + 1):
    for i in range(1, N + 1):
        c0 = cost[i - 1][j - 1]
        c1 = cost[i - 1][j]
        c2 = cost[i][j - 1]
        min_c = min(c0, c1, c2)
        if min_c == c0:
            c, t = c0, 0
        elif min_c == c1:
            c, t = c1, 1
        else:
            c, t = c2, 2
        cost[i][j] = x[i - 1][j - 1] + c
        trace[i][j] = t

print("Loop has finished.")  
