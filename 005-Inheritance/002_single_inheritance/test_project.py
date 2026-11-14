import unittest

from project.animal import Animal
from project.dog import Dog


class TestDog(unittest.TestCase):
    def test_dog_inherits_animal(self):
        dog = Dog()
        self.assertIsInstance(dog, Animal)
        self.assertEqual(dog.eat(), "eating...")
        self.assertEqual(dog.bark(), "barking...")


if __name__ == "__main__":
    unittest.main()
