from unittest.mock import MagicMock

globals = MagicMock()

channel = MagicMock()
b = MagicMock()
self = MagicMock()

self.dirty_rects = [(i, i + 1, i + 2, i + 3) for i in range(1000 * 100)]

# Loop Unrolling Optimization
print("Loop Unrolling Loop is starting...")

num_rects = len(self.dirty_rects)
i = 0
while i < num_rects - 1:  # Unroll by processing two rectangles per iteration
    rect1 = self.dirty_rects[i]
    rect2 = self.dirty_rects[i + 1]

    # Process the first rectangle
    channel.write_int(b, rect1[0])
    channel.write_int(b, rect1[1])
    channel.write_int(b, rect1[2])
    channel.write_int(b, rect1[3])

    # Process the second rectangle
    channel.write_int(b, rect2[0])
    channel.write_int(b, rect2[1])
    channel.write_int(b, rect2[2])
    channel.write_int(b, rect2[3])

    i += 2

# Handle the last rectangle if the count is odd
if num_rects % 2 != 0:
    rect = self.dirty_rects[-1]
    channel.write_int(b, rect[0])
    channel.write_int(b, rect[1])
    channel.write_int(b, rect[2])
    channel.write_int(b, rect[3])

print("Loop Unrolling Loop has finished.")
