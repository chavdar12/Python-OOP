import runpy
import unittest
from pathlib import Path

Circle = runpy.run_path(str(Path(__file__).with_name("003.py")))["Circle"]


class TestCircle(unittest.TestCase):
    def test_area_and_circumference(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.get_area(), 314.0)
        self.assertAlmostEqual(circle.get_circumference(), 62.8)

    def test_set_radius(self):
        circle = Circle(10)
        circle.set_radius(1)
        self.assertAlmostEqual(circle.get_area(), 3.14)


if __name__ == "__main__":
    unittest.main()
