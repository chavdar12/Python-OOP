import unittest

from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.cold_beverage import ColdBeverage
from project.beverage.hot_beverage import HotBeverage
from project.beverage.tea import Tea
from project.food.cake import Cake
from project.food.dessert import Dessert
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.salmon import Salmon
from project.food.soup import Soup
from project.food.starter import Starter
from project.product import Product


class TestRestaurant(unittest.TestCase):
    def test_hierarchy(self):
        expected = {Beverage: Product, HotBeverage: Beverage, ColdBeverage: Beverage, Coffee: HotBeverage,
                    Tea: HotBeverage, Food: Product, Starter: Food, Soup: Starter, MainDish: Food,
                    Salmon: MainDish, Dessert: Food, Cake: Dessert}
        for cls, parent in expected.items():
            with self.subTest(cls=cls.__name__):
                self.assertIs(cls.__bases__[0], parent)

    def test_product_and_beverage(self):
        beverage = Beverage("coffee", 2.5, 50)
        self.assertEqual((beverage.name, beverage.price, beverage.milliliters), ("coffee", 2.5, 50))

    def test_coffee_defaults(self):
        coffee = Coffee("Longo", 77.11)
        self.assertEqual((coffee.price, coffee.milliliters, coffee.caffeine), (3.50, 50, 77.11))

    def test_food(self):
        soup = Soup("fish soup", 9.90, 230)
        self.assertEqual((soup.name, soup.price, soup.grams), ("fish soup", 9.90, 230))
        self.assertEqual(Salmon("Salmon", 19.66).grams, 22)

    def test_cake_defaults(self):
        cake = Cake("CAKE")
        self.assertEqual((cake.price, cake.grams, cake.calories), (5, 250, 1000))


if __name__ == "__main__":
    unittest.main()
