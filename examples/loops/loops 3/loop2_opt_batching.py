from unittest.mock import MagicMock

globals = MagicMock()

file = MagicMock()
filename = MagicMock()
partials = {}
os = MagicMock()
partials_dir = MagicMock()
open = MagicMock()

mock_filenames = [f"file_{i}.html" for i in range(80000)]

os.listdir.return_value = mock_filenames

open.return_value.__enter__.return_value.read.return_value = "mock_file_content"

print("Batching Loop is starting...")

batch_size = 5  # Process files in batches of 5
filenames = os.listdir(partials_dir)
num_files = len(filenames)

# Process filenames in batches
for batch_start in range(0, num_files, batch_size):
    batch_end = min(batch_start + batch_size, num_files)
    batch_partials = {}  # Temporary storage for the batch
    for filename in filenames[batch_start:batch_end]:
        if filename.endswith('.html'):
            with open(os.path.join(partials_dir, filename), 'r', encoding='utf8') as file:
                batch_partials[filename[:-5]] = file.read()
    partials.update(batch_partials)  # Update main partials in bulk

print("Batching Loop has finished.")

