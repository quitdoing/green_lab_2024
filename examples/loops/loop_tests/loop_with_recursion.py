def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def loop_with_recursion():
    a = [0] * 35
    for i in range(35):
        a[i] = fibonacci_recursive(i + 2) + i
    return a
    
loop_with_recursion()
