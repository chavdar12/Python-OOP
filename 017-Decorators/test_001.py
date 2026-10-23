import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("001.py")))


class TestNumberIncrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(ns["number_increment"]([1, 2, 3]), [2, 3, 4])


if __name__ == "__main__":
    unittest.main()
