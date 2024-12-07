from unittest.mock import MagicMock

globals = MagicMock()

chunks = MagicMock()
text = MagicMock()
sizes = [10, 20, 30, 40, 50]
text = "This is a mock text that is going to be very long. " * 50000

# Loop execution starts here
print("Batching Loop is starting...")

batch_size = 4
for size in sizes:
    i = 0
    while i + size <= len(text):
        temp_chunks = []
        for _ in range(batch_size):
            if i + size <= len(text):  
                temp_chunks.append(text[i:i + size])
                i += size
            else:
                break
        #  chunks
        chunks.extend(temp_chunks)

print("Batching Loop has finished.")
# print(chunks)  
