import math

def loop_no_collapsing():
    a = [[0] * 4000] * 8000
    for i in range(8000):
        for j in range(4000):
            a[i][j] = (i * j) ** 2 * math.sin(i) * math.cos(i)
    return a
    
loop_no_collapsing()
