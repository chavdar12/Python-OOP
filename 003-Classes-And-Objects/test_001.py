import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Vehicle = runpy.run_path(str(Path(__file__).with_name("001.py")))["Vehicle"]


class TestVehicle(unittest.TestCase):
    def test_defaults(self):
        car = Vehicle(20)
        self.assertEqual((car.mileage, car.max_speed, car.gadgets), (20, 150, []))

    def test_gadgets_not_shared(self):
        first, second = Vehicle(1), Vehicle(2)
        first.gadgets.append("Hudly Wireless")
        self.assertEqual(second.gadgets, [])


if __name__ == "__main__":
    unittest.main()
