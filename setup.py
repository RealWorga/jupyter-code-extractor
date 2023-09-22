from setuptools import setup, find_packages

setup(
    name='jupyter-code-extractor',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jupyter-code-extractor=extract_code_jupyter.cli:main',
        ],
    },
    author="Hamed Haghjo",
    author_email="hamedhaghjo@hotmail.com",
    description="CLI tool to extract the code cells of a jupyter notebook into a .txt file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RealWorga/jupyter-code-extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
