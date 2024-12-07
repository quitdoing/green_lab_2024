from unittest.mock import MagicMock

globals = MagicMock()

channel = MagicMock()
b = MagicMock()
self = MagicMock()

self.dirty_rects = [(i, i + 1, i + 2, i + 3) for i in range(1000 * 100)]

# Batching Optimization
print("Batching Loop is starting...")

batch_size = 16  # Process 16 rectangles per batch
num_rects = len(self.dirty_rects)

batch_buffer = []  # Temporary buffer for batched writes
for i, rect in enumerate(self.dirty_rects):
    batch_buffer.extend(rect)  # Add the rectangle's data to the batch buffer

    # Write the batch when the buffer is full or at the end of the data
    if len(batch_buffer) >= batch_size * 4 or i == num_rects - 1:
        channel.write_batch(b, batch_buffer)  # Simulate batch write
        batch_buffer = []  # Clear the buffer

print("Batching Loop has finished.")
