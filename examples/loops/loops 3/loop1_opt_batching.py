from unittest.mock import MagicMock

globals = MagicMock()

self = MagicMock()
psutil = MagicMock()

self._m_avg = MagicMock()
self._lock = MagicMock()

max_iterations = 100000
batch_size = 10
iterations = 0

print("Loop is starting...")
while iterations < max_iterations:
    batch_samples = []
    
    for _ in range(min(batch_size, max_iterations - iterations)):
        cpu_p = psutil.cpu_percent(0.5) / 100.0
        batch_samples.append(cpu_p)
        iterations += 1

    with self._lock:
        for sample in batch_samples:
            self._m_avg.add_sample(sample)

print(f"Reached the maximum of {max_iterations} iterations. Exiting loop.")
print("Loop has finished.")
