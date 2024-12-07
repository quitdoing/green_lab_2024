from unittest.mock import MagicMock

globals = MagicMock()

segments = ["Segment {}".format(i) for i in range(50000 * 500)]
self = MagicMock()
last_word = MagicMock()
results = []
enumerate = MagicMock()

self.decimals = ['0.5', '1.5', '2.5']
self.multipliers = ['two', 'three']

BATCH_SIZE = 100  # Process segments in batches of 100
print("Batch processing is starting...") 

for batch_start in range(0, len(segments), BATCH_SIZE):
    batch = segments[batch_start:batch_start + BATCH_SIZE]
    for i, segment in enumerate(batch, start=batch_start):
        if len(segment.strip()) == 0:
            continue
        results.append(segment)
        if i == len(segments) - 1:
            continue
        last_word = segment.rsplit(maxsplit=2)[-1]
        if last_word in self.decimals or last_word in self.multipliers:
            results.append('point five')
        else:
            results.append('and a half')

print("Batch processing has finished.")
