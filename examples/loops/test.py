import os
import subprocess
import time

folder_path = './loops 3 2'

for filename in sorted(os.listdir(folder_path)):
    if filename.endswith('.py') & ("5" in filename):
        file_path = os.path.join(folder_path, filename)
        
        print(f"Running {filename}...")
        
        start_time = time.time()
        
        process = subprocess.run(['python', file_path], capture_output=True, text=True)
        
        execution_time = time.time() - start_time
        
        print(f"Output of {filename}:\n{process.stdout}")
        print(f"Execution time of {filename}: {execution_time:.2f} seconds\n")
