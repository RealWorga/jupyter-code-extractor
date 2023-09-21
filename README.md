# Code Extractor

A simple command-line tool for extracting code cells from Jupyter notebooks. Optionally, it allows extraction of all cell types including markdown.

## Installation

1. Package the project:
,,,
python setup.py sdist
,,,

2. Install the packaged distribution (Note: the version might depend on what is set in `setup.py`):
,,,
pip install --upgrade dist/code-extractor-0.1.tar.gz
,,,

## Usage

After installation, you can run the `code-extractor` directly from the CLI.

To extract all cell types, use the `--all-cells` option:
,,,
code-extractor --all-cells your_notebook.ipynb
,,,

Without the `--all-cells` option, only code cells will be extracted.

---

For any issues or contributions, please open an issue or pull request.
