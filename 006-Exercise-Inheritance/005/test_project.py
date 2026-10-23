import unittest

from project.drink import Drink
from project.food import Food
from project.product import Product
from project.product_repository import ProductRepository


class TestProduct(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(Food("apple").quantity, 15)
        self.assertEqual(Drink("water").quantity, 10)
        self.assertIsInstance(Food("apple"), Product)

    def test_decrease_and_increase(self):
        product = Product("x", 5)
        product.decrease(10)
        self.assertEqual(product.quantity, 5)
        product.decrease(5)
        product.increase(3)
        self.assertEqual(product.quantity, 3)

    def test_repr(self):
        self.assertEqual(repr(Food("apple")), "apple")


class TestProductRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ProductRepository()
        self.repo.add(Food("apple"))
        self.repo.add(Drink("water"))

    def test_find(self):
        self.assertEqual(self.repo.find("water").name, "water")
        self.assertIsNone(self.repo.find("nope"))

    def test_remove_all_matching(self):
        self.repo.add(Food("apple"))
        self.repo.remove("apple")
        self.assertEqual([p.name for p in self.repo.products], ["water"])

    def test_repr(self):
        self.assertEqual(repr(self.repo), "apple: 15\nwater: 10")


if __name__ == "__main__":
    unittest.main()
