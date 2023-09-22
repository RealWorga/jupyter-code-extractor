# Jupyter Code Cells to TXT

![PyPI version](https://img.shields.io/pypi/v/jupyter-code-extractor) ![Build Status](https://img.shields.io/github/actions/workflow/status/RealWorga/jupyter-code-extractor/workflow.yml?branch=main) ![License](https://img.shields.io/github/license/RealWorga/jupyter-code-extractor)

A simple command-line tool for extracting code cells from Jupyter notebooks. Optionally, it allows extraction of all cell types including markdown.

## Table of Contents
- [Installation](#installation)
  * [Development Installation](#development-installation)
  * [Local Installation](#local-installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

## Installation

## Development Installation

For those contributing and making changes to the codebase, it's often more efficient to install the package in 'editable' mode. This way, changes you make to the source immediately reflect in the installed package.

To install in editable mode:
```
python setup.py develop
```

This will set up a link to your source code, so you won't have to repackage and reinstall every time you make a change.
### Local Installation

1. Clean the `dist` directory to prevent old distributions:
```
rm -r dist/*
```

2. Package the project:
```
python setup.py sdist bdist_wheel
```

3. Install the packaged distribution (Note: the version might depend on what is set in `setup.py`):
```
pip install --upgrade dist/jupyter-code-extractor-0.1.tar.gz
```

## Usage

After installation, you can run the `jupyter-code-extractor` directly from the CLI.

To extract all cell types, use the `--all-cells` option:
```
jupyter-code-extractor --all-cells your_notebook.ipynb
```

Without the `--all-cells` option, only code cells will be extracted.

## Requirements

- Python 3.x
- Other dependencies can be found in the `requirements.txt` file.

## Contributing

For contributions, please create a fork, make your changes, and submit a pull request. Details on the development setup and guidelines can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

Once pull requests are approved and merged, maintainers will handle versioning and releases. New releases on GitHub will automatically trigger package updates on PyPI via GitHub Actions.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Changelog

For a detailed history of changes, see [CHANGELOG.md](./CHANGELOG.md).

- **0.1** - Initial release with basic features.
- **0.2** - ... (and so on for a few recent versions)

---

For any issues or contributions, please open an issue or pull request.
