import numpy as np


size = 150
nx0, ny0, nz0 = size, size, size
ldx, ldy, ldz = nx0, ny0, nz0
ist, iend = 0, nx0 - 1
jst, jend = 0, ny0 - 1


v = np.random.rand(5, nx0, ny0, nz0)

sum_norm = [0] * 5
block_size = 8

# Loop execution starts here
print("Loop is starting...") 

for m in range(5):
        for k_block in range(2, nz0 - 1, block_size):
            for j_block in range(jst, jend + 1, block_size):
                for i_block in range(ist, iend + 1, block_size):
                    for k in range(k_block, min(k_block + block_size, nz0 - 1)):
                        for j in range(j_block, min(j_block + block_size, jend + 1)):
                            for i in range(i_block, min(i_block + block_size, iend + 1)):
                                sum_norm[m] += v[m, i, j, k] ** 2

print("Loop has finished.")  
