
from unittest.mock import MagicMock

globals = MagicMock()

chunks = MagicMock()
text = MagicMock()
sizes = [10, 20, 30, 40, 50]
text = "This is a mock text that is going to be very long. " * 50000

print("Loop is starting...") 
for size in sizes:
    i = 0
    while i + size <= len(text):
        chunks.append(text[i:i + size])
        i += size

print("Loop has finished.")  