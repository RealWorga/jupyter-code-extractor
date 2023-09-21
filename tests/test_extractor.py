import unittest
import os
from extract_code_jupyter.extractor import extract_code_from_ipynb

class TestExtractor(unittest.TestCase):

    def tearDown(self):
        # Cleanup: remove the extracted file after test is done.
        if hasattr(self, 'output_filename') and os.path.exists(self.output_filename):
            os.remove(self.output_filename)

    def test_extraction_from_valid_notebook(self):
        notebook_path = "sample_notebooks/sample1.ipynb"
        expected_content = """
Cell 1:
```
print("Hello, World!")
```
"""

        self.output_filename = extract_code_from_ipynb(notebook_path)
        
        with open(self.output_filename, 'r') as f:
            extracted_content = f.read()

        self.assertEqual(extracted_content.strip(), expected_content.strip())

if __name__ == "__main__":
    unittest.main()