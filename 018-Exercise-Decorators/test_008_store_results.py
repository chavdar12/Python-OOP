import os
import runpy
import tempfile
import unittest
from pathlib import Path

SCRIPT = str(Path(__file__).with_name("008_store_results.py"))


class TestStoreResults(unittest.TestCase):
    def setUp(self):
        # the decorator appends to a file in the working directory; keep that out of the repo
        self.old_cwd = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.tmp.cleanup()

    def test_writes_results(self):
        store_results = runpy.run_path(SCRIPT)["store_results"]

        @store_results
        def sub(a, b):
            return a - b

        sub(5, 3)
        self.assertEqual(Path("09X_08_stored_results.txt").read_text(),
                         "Function 'add' was called. Result: 4\n"
                         "Function 'mult' was called. Result: 24\n"
                         "Function 'sub' was called. Result: 2\n")


if __name__ == "__main__":
    unittest.main()
