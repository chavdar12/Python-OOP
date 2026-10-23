import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("006.py")))


class TestTags(unittest.TestCase):
    def test_tags(self):
        self.assertEqual(ns["join_strings"]("Hello", " you!"), "<p>Hello you!</p>")
        self.assertEqual(ns["to_upper"]("hello"), "<h1>HELLO</h1>")


if __name__ == "__main__":
    unittest.main()
