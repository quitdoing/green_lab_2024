from unittest.mock import MagicMock

# Automatically mock any undefined global variables
globals = MagicMock()

# Define or mock variables used in the loop that might be undefined
nodes = MagicMock()
partitions = []
end = MagicMock()
Partition = MagicMock()
start = 0  # Assuming a numerical value for the start variable
total_memory = 100000  # Assuming a numerical value for total_memory
round = MagicMock()

nodes = [(f"Node {i}", MagicMock(memory=100)) for i in range(60000)]

BATCH_SIZE = 1000  # Process nodes in batches of 1000
print("Batch processing is starting...")

for batch_start in range(0, len(nodes), BATCH_SIZE):
    batch = nodes[batch_start:batch_start + BATCH_SIZE]
    for node in batch:
        end = round(start + node[1].memory / total_memory, 5)
        partitions.append(Partition(node[0], start, end))
        start = end

print("Batch processing has finished.")


