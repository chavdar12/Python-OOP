import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("003_even_numbers.py")))


class TestEvenNumbers(unittest.TestCase):
    def test_filters_even(self):
        self.assertEqual(ns["get_numbers"]([1, 2, 3, 4, 5]), [2, 4])


if __name__ == "__main__":
    unittest.main()
