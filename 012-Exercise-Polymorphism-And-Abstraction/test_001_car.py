import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("001_car.py")))


class TestCar(unittest.TestCase):
    def test_drive_with_air_conditioner(self):
        car = ns["Car"](20, 5)
        car.drive(3)
        self.assertAlmostEqual(car.fuel_quantity, 2.3)

    def test_drive_without_enough_fuel(self):
        car = ns["Car"](1, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 1)

    def test_refuel(self):
        car = ns["Car"](20, 5)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 30)


class TestTruck(unittest.TestCase):
    def test_drive_and_refuel_with_leak(self):
        truck = ns["Truck"](100, 15)
        truck.drive(5)
        self.assertAlmostEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertAlmostEqual(truck.fuel_quantity, 64.5)

    def test_vehicle_is_abstract(self):
        with self.assertRaises(TypeError):
            ns["Vehicle"]()


if __name__ == "__main__":
    unittest.main()
