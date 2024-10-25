from unittest.mock import MagicMock

globals = MagicMock()

self = MagicMock()
cpu_p = MagicMock()
psutil = MagicMock()

self._m_avg = MagicMock()
self._lock = MagicMock()

max_iterations = 100000
iterations = 0

print("Loop is starting...")
while True:
    if iterations >= max_iterations:
        print(f"Reached the maximum of {max_iterations} iterations. Exiting loop.")
        break

    cpu_p = psutil.cpu_percent(0.5) / 100.0
    with self._lock:
        self._m_avg.add_sample(cpu_p)

    iterations += 1

print("Loop has finished.")
