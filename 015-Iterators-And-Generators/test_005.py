import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    gen_range = runpy.run_path(str(Path(__file__).with_name("005.py")))["gen_range"]


class TestGenRange(unittest.TestCase):
    def test_inclusive(self):
        self.assertEqual(list(gen_range(1, 10)), list(range(1, 11)))


if __name__ == "__main__":
    unittest.main()
