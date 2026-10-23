import contextlib
import io
import math
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("004.py")))


class TestShapes(unittest.TestCase):
    def test_shape_is_abstract(self):
        with self.assertRaises(TypeError):
            ns["Shape"]()

    def test_circle(self):
        circle = ns["Circle"](5)
        self.assertAlmostEqual(circle.calculate_area(), 25 * math.pi)
        self.assertAlmostEqual(circle.calculate_perimeter(), 10 * math.pi)

    def test_rectangle(self):
        rectangle = ns["Rectangle"](10, 20)
        self.assertEqual((rectangle.calculate_area(), rectangle.calculate_perimeter()), (200, 60))


if __name__ == "__main__":
    unittest.main()
