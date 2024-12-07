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

print("Cache Blocking Loop is starting...")

block_size = 5  # Process 5 files in one block
filenames = os.listdir(partials_dir)  # Get all filenames at once
num_files = len(filenames)

# Process filenames in blocks
for block_start in range(0, num_files, block_size):
    block_end = min(block_start + block_size, num_files)
    for filename in filenames[block_start:block_end]:
        if filename.endswith('.html'):
            with open(os.path.join(partials_dir, filename), 'r', encoding='utf8') as file:
                partials[filename[:-5]] = file.read()

print("Cache Blocking Loop has finished.")

