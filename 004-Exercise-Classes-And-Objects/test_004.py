import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    PizzaDelivery = runpy.run_path(str(Path(__file__).with_name("004.py")))["PizzaDelivery"]


class TestPizzaDelivery(unittest.TestCase):
    def setUp(self):
        self.pizza = PizzaDelivery("Margarita", 11, {"cheese": 2, "tomatoes": 1})

    def test_add_extra(self):
        self.pizza.add_extra("mozzarella", 1, 0.5)
        self.pizza.add_extra("cheese", 1, 1)
        self.assertEqual(self.pizza.ingredients, {"cheese": 3, "tomatoes": 1, "mozzarella": 1})
        self.assertEqual(self.pizza.price, 12.5)

    def test_remove_ingredient_errors(self):
        self.assertEqual(self.pizza.remove_ingredient("bacon", 1, 2.5),
                         "Wrong ingredient selected! We do not use bacon in Margarita!")
        self.assertEqual(self.pizza.remove_ingredient("tomatoes", 2, 0.5),
                         "Please check again the desired quantity of tomatoes!")

    def test_remove_ingredient(self):
        self.pizza.remove_ingredient("cheese", 2, 1)
        self.assertEqual(self.pizza.ingredients["cheese"], 0)
        self.assertEqual(self.pizza.price, 9)

    def test_make_order_locks_pizza(self):
        self.assertEqual(self.pizza.make_order(),
                         "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 11lv.")
        msg = "Pizza Margarita already prepared, and we can't make any changes!"
        self.assertEqual(self.pizza.add_extra("cheese", 1, 1), msg)
        self.assertEqual(self.pizza.remove_ingredient("cheese", 1, 1), msg)


if __name__ == "__main__":
    unittest.main()
