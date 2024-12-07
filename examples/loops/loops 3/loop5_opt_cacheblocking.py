
from unittest.mock import MagicMock

globals = MagicMock()

chunks = MagicMock()
text = MagicMock()
sizes = [10, 20, 30, 40, 50]
text = "This is a mock text that is going to be very long. " * 50000

# Loop execution starts here
print("Loop is starting...") 
block_size = 1024  
for size in sizes:
    for block_start in range(0, len(text), block_size):
        block_end = min(block_start + block_size, len(text))
        while i + size <= block_end:
            chunks.append(text[i:i + size])
            i += size


print("Loop has finished.")  
