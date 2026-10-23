import unittest

from project.food import Food
from project.fruit import Fruit


class TestFruit(unittest.TestCase):
    def test_fruit_is_food(self):
        fruit = Fruit("banana", "01/01/2021")
        self.assertIsInstance(fruit, Food)
        self.assertEqual((fruit.name, fruit.expiration_date), ("banana", "01/01/2021"))


if __name__ == "__main__":
    unittest.main()
