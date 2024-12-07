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

print("Loop is starting...")

filenames = os.listdir(partials_dir)  # Get the list of files
num_files = len(filenames)

# Process files in batches of 2 (unrolling factor = 2)
i = 0
while i < num_files - 1:
    file1 = filenames[i]
    file2 = filenames[i + 1]

    # Handle the first file
    if file1.endswith('.html'):
        with open(os.path.join(partials_dir, file1), 'r', encoding='utf8') as f1:
            partials[file1[:-5]] = f1.read()

    # Handle the second file
    if file2.endswith('.html'):
        with open(os.path.join(partials_dir, file2), 'r', encoding='utf8') as f2:
            partials[file2[:-5]] = f2.read()

    i += 2  # Move to the next batch

# Handle the remaining file if the count is odd
if num_files % 2 != 0:
    file_last = filenames[-1]
    if file_last.endswith('.html'):
        with open(os.path.join(partials_dir, file_last), 'r', encoding='utf8') as f_last:
            partials[file_last[:-5]] = f_last.read()

print("Loop has finished.")
