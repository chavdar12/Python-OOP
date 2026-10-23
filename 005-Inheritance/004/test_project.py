import unittest

from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle


class TestSportsCar(unittest.TestCase):
    def test_multilevel_inheritance(self):
        car = SportsCar()
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car, Vehicle)
        self.assertEqual((car.race(), car.drive(), car.move()), ("racing...", "driving...", "moving..."))


if __name__ == "__main__":
    unittest.main()
