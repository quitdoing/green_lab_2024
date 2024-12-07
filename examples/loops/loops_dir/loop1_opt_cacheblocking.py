from unittest.mock import MagicMock
import time

globals = MagicMock()

self = MagicMock()
psutil = MagicMock()

self._m_avg = MagicMock()
self._lock = MagicMock()

max_iterations = 100000
iterations = 0

cpu_cache = None
cache_duration = 1
last_cache_time = 0

print("Loop is starting...")

while iterations < max_iterations:
    current_time = time.time()
    
    if cpu_cache is None or current_time - last_cache_time > cache_duration:
        cpu_cache = psutil.cpu_percent(0.5) / 100.0
        last_cache_time = current_time

    with self._lock:
        self._m_avg.add_sample(cpu_cache)

    iterations += 1

print("Loop has finished.")
