import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    take_skip = runpy.run_path(str(Path(__file__).with_name("001_take_skip.py")))["take_skip"]


class TestTakeSkip(unittest.TestCase):
    def test_take_skip(self):
        self.assertEqual(list(take_skip(2, 6)), [0, 2, 4, 6, 8, 10])
        self.assertEqual(list(take_skip(10, 5)), [0, 10, 20, 30, 40])


if __name__ == "__main__":
    unittest.main()
