from setuptools import setup, find_packages

setup(
    name='code-extractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'code-extractor=extract_code_jupyter.cli:main',
        ],
    },
)
