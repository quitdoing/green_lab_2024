import ast
import astor
import os
from unittest.mock import MagicMock

# Use AST to extract the loop and ensure correct indentation
def extract_loops_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())  # Parse the entire file into an AST

    loops = []  # Store all loops found
    for node in ast.walk(tree):  # Traverse all AST nodes
        if isinstance(node, (ast.For, ast.While)):  # Check if it's a loop
            loops.append(node)

    return loops

# Generate scaffold for each loop using AST
def create_scaffolding(loop_node):
    loop_code = astor.to_source(loop_node)  # Convert AST node back to source code

    # Use AST to analyze the loop code and detect undefined variables
    class UndefinedVariableFinder(ast.NodeVisitor):
        def __init__(self):
            self.undefined_vars = set()

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load):
                self.undefined_vars.add(node.id)

    # Find undefined variables in the loop
    finder = UndefinedVariableFinder()
    finder.visit(loop_node)
    
    # Mock all undefined variables
    mock_vars = "\n".join([f"{var} = MagicMock()" for var in finder.undefined_vars])

    # Generate scaffold code with mocking for all undefined variables
    mock_code = f"""
from unittest.mock import MagicMock

# Automatically mock any undefined global variables
globals = MagicMock()

# Define or mock variables used in the loop that might be undefined
{mock_vars}

# Loop execution starts here
print("Loop is starting...")
{loop_code}
print("Loop has finished.")
"""

    return mock_code

# Process all loops in a repository, and save them in a single output folder
def process_loops_in_repo(repo_directory, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist

    loop_count = 0  # Keep track of loop files
    # Find all Python files in the repo
    for root, _, files in os.walk(repo_directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                loops = extract_loops_from_file(file_path)  # Extract loops from file
                for i, loop in enumerate(loops):
                    scaffold_code = create_scaffolding(loop)  # Create scaffolding code
                    output_file_path = os.path.join(output_folder, f"scaffolded_loop_{loop_count}.py")
                    with open(output_file_path, "w", encoding="utf-8") as output_file:
                        output_file.write(scaffold_code)
                    loop_count += 1  # Increment the count to ensure unique filenames
                    print(f"Generated scaffold for loop {loop_count} in {file_path}")

# Specify the repository and output folder paths
if __name__ == "__main__":
    repo_dir = "/Users/candice/Python"  # Specify the repo path here
    output_dir = "/Users/candice/loops_output"  # Set output folder under /Users/candice
    process_loops_in_repo(repo_dir, output_dir)
