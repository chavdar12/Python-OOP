import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    custom_range = runpy.run_path(str(Path(__file__).with_name("001.py")))["custom_range"]


class TestCustomRange(unittest.TestCase):
    def test_inclusive_range(self):
        self.assertEqual(list(custom_range(1, 10)), list(range(1, 11)))
        self.assertEqual(list(custom_range(5, 4)), [])


if __name__ == "__main__":
    unittest.main()
