def loop_no_cache_blocking():
    a = [[0] * 20000] * 20000
    b = [[2] * 20000] * 20000
    for i in range(20000):
        for j in range(20000):
            a[i][j] = b[i][j] + 1
    return a

loop_no_cache_blocking
