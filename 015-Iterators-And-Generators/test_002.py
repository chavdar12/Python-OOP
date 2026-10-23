import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    reverse_iter = runpy.run_path(str(Path(__file__).with_name("002.py")))["reverse_iter"]


class TestReverseIter(unittest.TestCase):
    def test_reverses(self):
        self.assertEqual(list(reverse_iter([1, 2, 3, 4])), [4, 3, 2, 1])
        self.assertEqual(list(reverse_iter([])), [])


if __name__ == "__main__":
    unittest.main()
