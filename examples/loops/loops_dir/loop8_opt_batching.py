import numpy as np


size = 150
nx0, ny0, nz0 = size, size, size
ldx, ldy, ldz = nx0, ny0, nz0
ist, iend = 0, nx0 - 1
jst, jend = 0, ny0 - 1


v = np.random.rand(5, nx0, ny0, nz0)

sum_norm = [0] * 5

# Loop execution starts here
print("Batching Loop is starting...")

batch_size = 4  # Process 4 elements per batch
for k in range(2, nz0 - 1):
    for j in range(jst, jend + 1):
        for i_batch_start in range(ist, iend + 1, batch_size):
            i_batch_end = min(i_batch_start + batch_size, iend + 1)
            
            # Temporary batch accumulators
            temp_sums = [0] * 5  
            
            for i in range(i_batch_start, i_batch_end):  # Batch over 'i'
                for m in range(5):
                    temp_sums[m] += v[m, i, j, k] ** 2
            
            # Update the global sum_norm after processing the batch
            for m in range(5):
                sum_norm[m] += temp_sums[m]

print("Batching Loop has finished.")
