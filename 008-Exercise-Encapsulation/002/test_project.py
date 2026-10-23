import unittest

from project.dough import Dough
from project.pizza import Pizza


class TestPizzaValidation(unittest.TestCase):
    """Complements test.py with the validation edge cases."""

    def setUp(self):
        self.dough = Dough("White Flour", "Mixing", 200)

    def test_negative_capacity_rejected(self):
        for capacity in [0, -1]:
            with self.subTest(capacity=capacity), self.assertRaises(ValueError) as ctx:
                Pizza("Margherita", self.dough, capacity)
            self.assertEqual(str(ctx.exception), "The topping's capacity cannot be less or equal to zero")

    def test_missing_dough_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            Pizza("Margherita", None, 2)
        self.assertEqual(str(ctx.exception), "You should add dough to the pizza")

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError) as ctx:
            Pizza("", self.dough, 2)
        self.assertEqual(str(ctx.exception), "The name cannot be an empty string")


if __name__ == "__main__":
    unittest.main()
