
from unittest.mock import MagicMock

globals = MagicMock()

file = MagicMock()
filename = MagicMock()
partials = MagicMock()
os = MagicMock()
partials_dir = MagicMock()
open = MagicMock()
mock_filenames = [f"file_{i}.html" for i in range(80000)]

os.listdir.return_value = mock_filenames

open.return_value.__enter__.return_value.read.return_value = "mock_file_content"
print("Loop is starting...")
for filename in os.listdir(partials_dir):
    if filename.endswith('.html'):
        with open(os.path.join(partials_dir, filename), 'r', encoding='utf8'
            ) as file:
            partials[filename[:-5]] = file.read()

print("Loop has finished.")
