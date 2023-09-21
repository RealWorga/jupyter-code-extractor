import json
import os
import re

def extract_code_from_ipynb(ipynb_file, all_cells=False):
    if not os.path.exists(ipynb_file):
        print(f"Error: File {ipynb_file} does not exist.")
        return

    with open(ipynb_file, 'r') as f:
        try:
            notebook = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: The file {ipynb_file} is not a valid JSON file or is corrupted.")
            return

    if 'cells' not in notebook:
        print(f"Error: The file {ipynb_file} doesn't seem to be a valid Jupyter notebook.")
        return

    def clean_content(content):
        content = re.sub(r"<div.*?>", "", content)
        content = re.sub(r"</div>", "", content)
        content = content.strip()
        return content


    if all_cells:
        cells = [f"Cell {idx + 1}:\n```\n{clean_content(''.join(cell['source']))}\n```" for idx, cell in enumerate(notebook['cells'])]
    else:
        #Sequential numbering for the code cells instead of their actual notebook index!
        code_cell_idx = 1
        cells = []
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                cells.append(f"Cell {code_cell_idx}:\n```\n{clean_content(''.join(cell['source']))}\n```")
                code_cell_idx += 1

    if not cells:
        print(f"Note: No relevant cells found in {ipynb_file}.")
        return

    base_filename = os.path.splitext(ipynb_file)[0]
    output_filename = f"{base_filename}_all_cells_extracted.txt" if all_cells else f"{base_filename}_code_extracted.txt"

    with open(output_filename, 'w') as f:
        f.write("\n\n".join(cells))

    print(f"Content extracted successfully to {output_filename}")
    return output_filename
