from extract_code_jupyter.extractor import extract_code_from_ipynb
import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract content from Jupyter Notebook')
    parser.add_argument('notebook_path', help='Path to the Jupyter Notebook')
    parser.add_argument('--all-cells', action='store_true', help='Extract all cells (including markdown)')
    args = parser.parse_args()

    extract_code_from_ipynb(args.notebook_path, all_cells=args.all_cells)

if __name__ == "__main__":
    main()
