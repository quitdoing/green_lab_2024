import time

# Start a loop that will run for approximately 1 minute
start_time = time.time()
while time.time() - start_time < 10:  # Loop will run for 60 seconds (1 minute)
    for i in range(1000000):
        pass  # A simple operation to keep the CPU busy
    time.sleep(0.01)  # A small delay to slightly slow down the loop
#def fibonacci_recursive(n):
 #  if n <= 0:
  #     return 0
   #elif n == 1:
    #   return 1
   #else:
    #   return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


#def energy_intensive_loop(num_iterations):
 #  results = []
  # for i in range(num_iterations):
       # 计算第 i 个 Fibonacci 数并将其添加到结果列表中
   #    result = fibonacci_recursive(i + 20)  # 20 使得计算的 Fibonacci 数更大
    #   results.append(result)
     #  print(f"Fibonacci({i + 20}) = {result}")


# 调用函数并指定迭代次数
#energy_intensive_loop(30)
