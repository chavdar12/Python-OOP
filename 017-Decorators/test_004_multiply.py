import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("004_multiply.py")))


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(ns["add_ten"](6), 80)
        self.assertEqual(ns["multiply"](3)(lambda n: n + 10)(3), 39)


if __name__ == "__main__":
    unittest.main()
