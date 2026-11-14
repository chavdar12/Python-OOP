import unittest

from project.car import Car
from project.cross_motorcycle import CrossMotorcycle
from project.family_car import FamilyCar
from project.motorcycle import Motorcycle
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.vehicle import Vehicle


class TestVehicles(unittest.TestCase):
    def test_fuel_consumption(self):
        expected = {Vehicle: 1.25, Motorcycle: 1.25, CrossMotorcycle: 1.25, RaceMotorcycle: 8,
                    Car: 3, FamilyCar: 3, SportCar: 10}
        for cls, consumption in expected.items():
            with self.subTest(cls=cls.__name__):
                self.assertEqual(cls(50, 150).fuel_consumption, consumption)

    def test_drive_uses_fuel(self):
        car = FamilyCar(150, 150)
        car.drive(50)
        self.assertEqual(car.fuel, 0)

    def test_drive_without_enough_fuel_does_nothing(self):
        vehicle = Vehicle(50, 150)
        vehicle.drive(100)
        self.assertEqual(vehicle.fuel, 50)


if __name__ == "__main__":
    unittest.main()
