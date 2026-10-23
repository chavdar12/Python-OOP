import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("002.py")))


class TestEvenParameters(unittest.TestCase):
    def test_even_parameters(self):
        error = "Please use only even numbers!"
        self.assertEqual(ns["add"](2, 4), 6)
        self.assertEqual(ns["add"]("Peter", 1), error)
        self.assertEqual(ns["multiply"](2, 4, 6, 8), 384)
        self.assertEqual(ns["multiply"](2, 4, 9, 8), error)


if __name__ == "__main__":
    unittest.main()
