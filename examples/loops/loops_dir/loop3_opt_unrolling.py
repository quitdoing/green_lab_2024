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

print("Loop is starting...")
nodes = [(f"Node {i}", MagicMock(memory=100)) for i in range(60000)]
i = 0
while i < len(nodes) - 1:
    end1 = round(start + nodes[i][1].memory / total_memory, 5)
    partitions.append(Partition(nodes[i][0], start, end1))
    
    start = end1
    end2 = round(start + nodes[i + 1][1].memory / total_memory, 5)
    partitions.append(Partition(nodes[i + 1][0], start, end2))
    
    start = end2
    i += 2

if len(nodes) % 2 != 0:
    end = round(start + nodes[i][1].memory / total_memory, 5)
    partitions.append(Partition(nodes[i][0], start, end))

print("Loop has finished.")
