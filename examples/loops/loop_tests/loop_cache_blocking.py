def loop_cache_blocking():
    a = [[0] * 20000] * 20000
    b = [[2] * 20000] * 20000
    block_size = 10
    for i in range(0, 20000, block_size):
        for j in range(0, 20000, block_size):
            for ii in range(i, min(i + block_size, 20000)):
                for jj in range(j, min(j + block_size, 20000)):
                    a[ii][jj] = b[ii][jj] + 1
    return a
    
loop_cache_blocking()
