
from unittest.mock import MagicMock

globals = MagicMock()

channel = MagicMock()
b = MagicMock()
self = MagicMock()


self.dirty_rects = [(i, i + 1, i + 2, i + 3) for i in range(1000 * 100)]


print("Loop is starting...") 
for rect in self.dirty_rects:
    channel.write_int(b, rect[0])
for rect in self.dirty_rects:
    channel.write_int(b, rect[1])
for rect in self.dirty_rects:
    channel.write_int(b, rect[2])
for rect in self.dirty_rects:
    channel.write_int(b, rect[3])

print("Loop has finished.")  
