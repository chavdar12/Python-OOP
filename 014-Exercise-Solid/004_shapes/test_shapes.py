import contextlib
import io
import math
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("shapes.py")))


class TestAreaCalculator(unittest.TestCase):
    def test_total_area(self):
        shapes = [ns["Rectangle"](1, 6), ns["Triangle"](2, 3), ns["Circle"](1)]
        self.assertAlmostEqual(ns["AreaCalculator"](shapes).total_area, 9 + math.pi)

    def test_requires_list(self):
        with self.assertRaises(AssertionError):
            ns["AreaCalculator"]((ns["Rectangle"](1, 1),))


if __name__ == "__main__":
    unittest.main()
