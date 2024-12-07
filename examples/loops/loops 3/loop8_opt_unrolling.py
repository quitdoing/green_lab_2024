import numpy as np


size = 150
nx0, ny0, nz0 = size, size, size

v = np.random.rand(5, nx0, ny0, nz0)
sum_norm_0, sum_norm_1, sum_norm_2, sum_norm_3, sum_norm_4 = 0, 0, 0, 0, 0

# Loop execution starts here
print("Loop is starting...") 

for k in range(2, nz0 - 1):
    for j in range(jst, jend + 1):
        for i in range(ist, iend + 1):
            sum_norm_0 += v[0, i, j, k] ** 2
            sum_norm_1 += v[1, i, j, k] ** 2
            sum_norm_2 += v[2, i, j, k] ** 2
            sum_norm_3 += v[3, i, j, k] ** 2
            sum_norm_4 += v[4, i, j, k] ** 2
            
print("Loop has finished.")  
