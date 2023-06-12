import unittest
import filecmp
from zeppelinto import ZeppelinConverter

class TestConvertToJupyterNotebook(unittest.TestCase):

    def test_convert_to_jupyter_notebook(self):
        file_path = "tests/test_input/sample-notebook.json"
        zep = ZeppelinConverter()
        zep.load_notebook(file_path)
        zep.to_jupyter_notebook("tests/test_output/sample-test.ipynb")
        self.assertTrue(filecmp.cmp("tests/test_input/sample-test.ipynb", "tests/test_output/sample-test.ipynb"))

if __name__ == '__main__':
    unittest.main()




