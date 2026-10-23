import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("003.py")))


class TestTagsStacking(unittest.TestCase):
    def test_bold_italic_underline(self):
        self.assertEqual(ns["greet"]("Peter"), "<b><i><u>Hello, Peter</u></i></b>")
        self.assertEqual(ns["greet_all"]("Peter", "George"), "<b><i><u>Hello, Peter, George</u></i></b>")


if __name__ == "__main__":
    unittest.main()
