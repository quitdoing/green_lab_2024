import time

# Start a loop that will run for approximately 1 minute
start_time = time.time()
while time.time() - start_time < 5:  # Loop will run for 60 seconds (1 minute)
    for i in range(1000000):
        pass  # A simple operation to keep the CPU busy
    time.sleep(0.01)  # A small delay to slightly slow down the loop
