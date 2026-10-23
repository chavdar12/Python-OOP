import unittest

from project.animals.birds import Hen, Owl
from project.animals.mammals import Cat, Dog, Mouse, Tiger
from project.food import Food, Fruit, Meat, Seed, Vegetable


class TestFood(unittest.TestCase):
    def test_food_is_abstract(self):
        with self.assertRaises(TypeError):
            Food(1)
        self.assertEqual(Seed(3).quantity, 3)


class TestAnimals(unittest.TestCase):
    def test_sounds(self):
        animals = {Owl("a", 1, 1): "Hoot Hoot", Hen("a", 1, 1): "Cluck", Mouse("a", 1, "r"): "Squeak",
                   Dog("a", 1, "r"): "Woof!", Cat("a", 1, "r"): "Meow", Tiger("a", 1, "r"): "ROAR!!!"}
        for animal, sound in animals.items():
            with self.subTest(animal=type(animal).__name__):
                self.assertEqual(animal.make_sound(), sound)

    def test_weight_gain_per_food_unit(self):
        cases = [(Owl("a", 10, 1), Meat(4), 11), (Hen("a", 10, 1), Seed(10), 13.5),
                 (Mouse("a", 10, "r"), Fruit(10), 11), (Dog("a", 10, "r"), Meat(10), 14),
                 (Cat("a", 10, "r"), Vegetable(10), 13), (Tiger("a", 10, "r"), Meat(2), 12)]
        for animal, food, weight in cases:
            with self.subTest(animal=type(animal).__name__):
                animal.feed(food)
                self.assertAlmostEqual(animal.weight, weight)
                self.assertEqual(animal.food_eaten, food.quantity)

    def test_refuses_wrong_food(self):
        cases = [(Owl("a", 10, 1), Vegetable(1)), (Mouse("a", 10, "r"), Meat(1)), (Dog("a", 10, "r"), Seed(1)),
                 (Cat("a", 10, "r"), Fruit(1)), (Tiger("a", 10, "r"), Vegetable(1))]
        for animal, food in cases:
            with self.subTest(animal=type(animal).__name__):
                self.assertEqual(animal.feed(food), f"{type(animal).__name__} does not eat {type(food).__name__}!")
                self.assertEqual(animal.food_eaten, 0)

    def test_repr(self):
        self.assertEqual(repr(Owl("Pip", 10, 10)), "Owl [Pip, 10, 10, 0]")
        self.assertEqual(repr(Dog("Ivan", 11, "Gabrovo")), "Dog [Ivan, 11, Gabrovo, 0]")


if __name__ == "__main__":
    unittest.main()
