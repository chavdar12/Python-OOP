import unittest

from project.animal import Animal
from project.bear import Bear
from project.gorilla import Gorilla
from project.lizard import Lizard
from project.mammal import Mammal
from project.reptile import Reptile
from project.snake import Snake


class TestZooHierarchy(unittest.TestCase):
    def test_parents(self):
        expected = {Mammal: Animal, Reptile: Animal, Bear: Mammal, Gorilla: Mammal, Lizard: Reptile, Snake: Reptile}
        for cls, parent in expected.items():
            with self.subTest(cls=cls.__name__):
                self.assertIs(cls.__bases__[0], parent)
                self.assertEqual(cls("Stella").name, "Stella")


if __name__ == "__main__":
    unittest.main()
