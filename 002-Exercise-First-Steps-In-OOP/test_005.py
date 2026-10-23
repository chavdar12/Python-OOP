import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Flower = runpy.run_path(str(Path(__file__).with_name("005.py")))["Flower"]


class TestFlower(unittest.TestCase):
    def setUp(self):
        self.flower = Flower("Lilly", 100)

    def test_not_happy_initially(self):
        self.assertEqual(self.flower.status(), "Lilly is not happy")

    def test_enough_water_makes_happy(self):
        self.flower.water(100)
        self.assertEqual(self.flower.status(), "Lilly is happy")

    def test_too_little_water_makes_unhappy_again(self):
        self.flower.water(100)
        self.flower.water(50)
        self.assertFalse(self.flower.is_happy)


if __name__ == "__main__":
    unittest.main()
