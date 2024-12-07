from unittest.mock import MagicMock

# Automatically mock any undefined global variables
globals = MagicMock()

# Define or mock variables used in the loop
nodes = MagicMock()
partitions = MagicMock()
Partition = MagicMock()
start = MagicMock()
total_memory = MagicMock()
round = MagicMock()

# Mock nodes as a list of tuples with node ID and memory
nodes = [(f"Node {i}", MagicMock(memory=100)) for i in range(60000)]
total_memory = sum(node[1] for node in nodes)  # Calculate total memory
start = 0.0  # Initialize start

# Mock Partition to simulate appending behavior
def Partition(node_id, start, end):
    return {"node_id": node_id, "start": start, "end": end}

partitions = []  # List to store partitions

# Batching Optimization
print("Batching Loop is starting...")

batch_size = 16  # Process 16 nodes per batch
for batch_start in range(0, len(nodes), batch_size):
    batch_end = min(batch_start + batch_size, len(nodes))  # Define batch range
    temp_partitions = []  # Temporary storage for batch partitions

    for node in nodes[batch_start:batch_end]:  # Process each node in the batch
        end = round(start + node[1] / total_memory, 5)  # Calculate end
        temp_partitions.append(Partition(node[0], start, end))  # Add partition to batch
        start = end  # Update start for the next node

    partitions.extend(temp_partitions)  # Append batch partitions to main list

print("Batching Loop has finished.")
#print(partitions)  # Output the partitions (for debugging)
