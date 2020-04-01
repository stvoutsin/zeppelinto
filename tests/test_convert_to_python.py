import unittest
import filecmp
from zeppelinTo import ZeppelinTo

class TestConvertToPython(unittest.TestCase):

    def test_convert_to_python(self):
        file_path = "tests/test_input/sample-notebook.json"
        zep = ZeppelinTo()
        zep.load_notebook(file_path)
        zep.to_python("tests/test_output/sample-test.py")
        self.assertTrue(filecmp.cmp("tests/test_input/sample-test.py", "tests/test_output/sample-test.py"))

if __name__ == '__main__':
    unittest.main()
