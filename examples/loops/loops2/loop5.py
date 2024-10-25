
from unittest.mock import MagicMock

globals = MagicMock()

nodes = MagicMock()
partitions = MagicMock()
end = MagicMock()
Partition = MagicMock()
start = MagicMock()
total_memory = MagicMock()
node = MagicMock()
round = MagicMock()

nodes = [(f"Node {i}", MagicMock(memory=100)) for i in range(60000)]

print("Loop is starting...")
for node in nodes:
    end = round(start + node[1].memory / total_memory, 5)
    partitions.append(Partition(node[0], start, end))
    start = end

print("Loop has finished.")