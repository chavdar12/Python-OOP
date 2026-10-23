import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest import mock


def run_with_input(value):
    out = io.StringIO()
    with mock.patch("builtins.input", return_value=value), contextlib.redirect_stdout(out):
        runpy.run_path(str(Path(__file__).with_name("001.py")))
    return out.getvalue()


class TestRhombus(unittest.TestCase):
    def test_size_3(self):
        self.assertEqual(run_with_input("3"), "  *\n * *\n* * *\n * *\n  *\n")

    def test_size_1(self):
        self.assertEqual(run_with_input("1"), "*\n")


if __name__ == "__main__":
    unittest.main()
