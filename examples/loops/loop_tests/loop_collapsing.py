import math

def loop_collapsing():
    a = [[0] * 4000] * 8000
    for k in range(32000000):
        i = k // 4000
        j = k % 4000
        a[i][j] = (i * j) ** 2 * math.sin(i) * math.cos(i)
    return a
    
loop_collapsing()
