import ast
import astor
import os
from unittest.mock import MagicMock

def extract_loops_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    loops = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)):
            loops.append(node)
    return loops

def create_scaffolding(loop_node):
    loop_code = astor.to_source(loop_node)

    class UndefinedVariableFinder(ast.NodeVisitor):
        def __init__(self):
            self.undefined_vars = set()
        def visit_Name(self, node):
            if isinstance(node.ctx, ast.Load):
                self.undefined_vars.add(node.id)

    finder = UndefinedVariableFinder()
    finder.visit(loop_node)
    mock_vars = "\n".join([f"{var} = MagicMock()" for var in finder.undefined_vars])

    mock_code = f"""
from unittest.mock import MagicMock

globals = MagicMock()

{mock_vars}

print("Loop is starting...")
{loop_code}
print("Loop has finished.")
"""
    return mock_code

def process_loops_in_repo(repo_directory, output_folder, output_txt_file):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    loop_count = 0

    with open(output_txt_file, "w", encoding="utf-8") as txt_output_file:
        for root, _, files in os.walk(repo_directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    loops = extract_loops_from_file(file_path)
                    for i, loop in enumerate(loops):
                        scaffold_code = create_scaffolding(loop)
                        loop_count += 1
                        output_file_path = os.path.join(output_folder, f"scaffolded_loop_{loop_count}.py")
                        with open(output_file_path, "w", encoding="utf-8") as output_file:
                            output_file.write(scaffold_code)
                        txt_output_file.write(f"# Loop {loop_count} from file: {file_path}\n")
                        txt_output_file.write(scaffold_code)
                        txt_output_file.write("\n" + "=" * 80 + "\n")
                        print(f"Generated scaffold for loop {loop_count} in {file_path}")

if __name__ == "__main__":
    repo_dir = "/Users/candice/exo"  # change here
    output_folder = "/Users/candice/loops_output" # change here
    output_txt_file = "/Users/candice/loops_output/scaffolded_loops.txt" # output
    process_loops_in_repo(repo_dir, output_folder, output_txt_file)
