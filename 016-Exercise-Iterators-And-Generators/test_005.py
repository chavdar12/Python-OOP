import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    solution = runpy.run_path(str(Path(__file__).with_name("005.py")))["solution"]


class TestSolution(unittest.TestCase):
    def test_take_halves(self):
        take, halves, integers = solution()
        self.assertEqual(take(5, halves()), [0.5, 1.0, 1.5, 2.0, 2.5])
        self.assertEqual(take(0, halves()), [])
        self.assertEqual(take(3, integers()), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
