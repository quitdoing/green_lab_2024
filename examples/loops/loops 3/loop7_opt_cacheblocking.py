from unittest.mock import MagicMock

globals = MagicMock()

channel = MagicMock()
b = MagicMock()
self = MagicMock()

self.dirty_rects = [(i, i + 1, i + 2, i + 3) for i in range(1000 * 100)]

# Cache Blocking Optimization
print("Cache Blocking Loop is starting...")

block_size = 16  # Process 16 rectangles per block
num_rects = len(self.dirty_rects)

# Process in blocks
for block_start in range(0, num_rects, block_size):
    block_end = min(block_start + block_size, num_rects)
    for rect in self.dirty_rects[block_start:block_end]:
        channel.write_int(b, rect[0])
        channel.write_int(b, rect[1])
        channel.write_int(b, rect[2])
        channel.write_int(b, rect[3])

print("Cache Blocking Loop has finished.")
