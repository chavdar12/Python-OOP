import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Point = runpy.run_path(str(Path(__file__).with_name("002_point.py")))["Point"]


class TestPoint(unittest.TestCase):
    def test_setters_and_str(self):
        p = Point(2, 4)
        self.assertEqual(str(p), "The point has coordinates (2,4)")
        p.set_x(3)
        p.set_y(5)
        self.assertEqual(str(p), "The point has coordinates (3,5)")


if __name__ == "__main__":
    unittest.main()
