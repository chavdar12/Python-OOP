import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog


class TestHierarchicalInheritance(unittest.TestCase):
    def test_cat(self):
        self.assertIsInstance(Cat(), Animal)
        self.assertEqual((Cat().meow(), Cat().eat()), ("meowing...", "eating..."))

    def test_dog(self):
        self.assertIsInstance(Dog(), Animal)
        self.assertEqual((Dog().bark(), Dog().eat()), ("barking...", "eating..."))


if __name__ == "__main__":
    unittest.main()
