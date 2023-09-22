from setuptools import setup, find_packages

setup(
    name='jupyter-code-extractor',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jupyter-code-extractor=extract_code_jupyter.cli:main',
        ],
    },
    author="Hamed Haghjo",
    author_email="hamedhaghjo@hotmail.com",
    url="https://github.com/RealWorga/jupyter-code-extractor",
)
