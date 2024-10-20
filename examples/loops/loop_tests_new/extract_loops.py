import ast
import importlib
import astor
import os
from unittest.mock import MagicMock

# Step 1: Use AST to extract the loop and ensure correct indentation
def extract_loops_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())  # Parse the entire file into an AST

    loops = []  # Store all loops found

    class AwaitFinder(ast.NodeVisitor):
        def __init__(self):
            self.has_await = False

        def visit_Await(self, node):
            self.has_await = True  # Found an await
            self.generic_visit(node)  # Continue visiting

    class YieldFinder(ast.NodeVisitor):
        def __init__(self):
            self.has_yield = False

        def visit_Yield(self, node):
            self.has_yield = True  # Found a yield
            self.generic_visit(node)  # Continue visiting

    class ReturnFinder(ast.NodeVisitor):
        def __init__(self):
            self.has_return = False

        def visit_Return(self, node):
            self.has_return = True  # Found a return
            self.generic_visit(node)  # Continue visiting

    class InfiniteLoopFinder(ast.NodeVisitor):
        def __init__(self):
            self.has_infinite_loop = False

        def visit_While(self, node):
            if isinstance(node.test, ast.Constant) and node.test.value is True:
                self.has_infinite_loop = True  # Found a while True loop
            self.generic_visit(node)  # Continue visiting

    for node in ast.walk(tree):  # Traverse all AST nodes
        if isinstance(node, (ast.For, ast.While)):  # Check if it's a loop
            # Check for await
            await_finder = AwaitFinder()
            await_finder.visit(node)

            # Check for yield
            yield_finder = YieldFinder()
            yield_finder.visit(node)

            # Check for return
            return_finder = ReturnFinder()
            return_finder.visit(node)

            # Check for infinite loop
            infinite_loop_finder = InfiniteLoopFinder()
            infinite_loop_finder.visit(node)

            if not await_finder.has_await and not yield_finder.has_yield and not return_finder.has_return and not infinite_loop_finder.has_infinite_loop:
                loops.append(node)

    return loops

# Step 2: Generate scaffold for each loop using AST
def create_scaffolding(loop_node):
    loop_code = astor.to_source(loop_node)  # Convert AST node back to source code

    # Determine the leading whitespace from the loop code
    leading_space = 4

    # Apply leading space to each line of the modified loop code
    indented_lines = []
    for line in loop_code.splitlines():
        # Add the same leading space to each line
        indented_lines.append(' ' * leading_space + line)

    # Join the indented lines back together
    loop_code_with_indent = '\n'.join(indented_lines)    

    # Use AST to analyze the loop code and detect undefined variables
    class UndefinedVariableFinder(ast.NodeVisitor):
        def __init__(self):
            self.undefined_vars = set()

        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load):  # Variable is being read, not assigned
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

# Step 3: Process all loops in a repository, and save them in a single output folder
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

def execute_python_files(output_folder):
    for file_name in os.listdir(output_folder):
        if file_name.endswith(".py"):
            file_path = os.path.join(output_folder, file_name)
            # 动态导入模块
            spec = importlib.util.spec_from_file_location(file_name[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # 执行模块

            print(f"Executed {file_name}")

# Step 4: Specify the repository and output folder paths
if __name__ == "__main__":
    repo_dir = "D:/1-coding/v4s/github"  # Specify the repo path here
    output_dir = "D:/1-coding/v4s/output"  # Set output folder
    process_loops_in_repo(repo_dir, output_dir)