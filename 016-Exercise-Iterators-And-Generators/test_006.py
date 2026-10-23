import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    fibonacci = runpy.run_path(str(Path(__file__).with_name("006.py")))["fibonacci"]


class TestFibonacci(unittest.TestCase):
    def test_first_numbers(self):
        generator = fibonacci()
        self.assertEqual([next(generator) for _ in range(7)], [0, 1, 1, 2, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()
