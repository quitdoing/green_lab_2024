from unittest.mock import MagicMock

globals = MagicMock()

segments = ["Segment {}".format(i) for i in range(50000 * 500)]
self = MagicMock()
last_word = MagicMock()
results = []
enumerate = MagicMock()

self.decimals = ['0.5', '1.5', '2.5']
self.multipliers = ['two', 'three']

print("Loop unrolling is starting...")

n = len(segments)
i = 0
while i < n:
    # Unrolling four iterations
    for j in range(4):
        if i + j >= n:
            break
        segment = segments[i + j]
        if len(segment.strip()) == 0:
            continue
        results.append(segment)
        if i + j == n - 1:
            continue
        last_word = segment.rsplit(maxsplit=2)[-1]
        if last_word in self.decimals or last_word in self.multipliers:
            results.append('point five')
        else:
            results.append('and a half')
    i += 4

print("Loop unrolling has finished.")
