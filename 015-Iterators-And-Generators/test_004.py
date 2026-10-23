import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    squares = runpy.run_path(str(Path(__file__).with_name("004.py")))["squares"]


class TestSquares(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(list(squares(5)), [1, 4, 9, 16, 25])


if __name__ == "__main__":
    unittest.main()
