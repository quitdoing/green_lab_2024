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
html_filenames = [f for f in os.listdir(partials_dir) if f.endswith('.html')]

partials = {filename[:-5]: open(os.path.join(partials_dir, filename), 'r', encoding='utf8').read()
            for filename in html_filenames}

print("Loop has finished.")
