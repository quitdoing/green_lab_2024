from unittest.mock import MagicMock

globals = MagicMock()

channel = MagicMock()
b = MagicMock()
self = MagicMock()

self.dirty_rects = [(i, i + 1, i + 2, i + 3) for i in range(1000 * 100)]

BATCH_SIZE = 100  # Process rectangles in batches of 100
print("Batch processing is starting...")

for batch_start in range(0, len(self.dirty_rects), BATCH_SIZE):
    batch = self.dirty_rects[batch_start:batch_start + BATCH_SIZE]
    for rect in batch:
        channel.write_int(b, rect[0])
        channel.write_int(b, rect[1])
        channel.write_int(b, rect[2])
        channel.write_int(b, rect[3])

print("Batch processing has finished.")
