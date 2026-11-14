import unittest

from project.child import Child
from project.person import Person


class TestChild(unittest.TestCase):
    def test_child_is_person(self):
        child = Child("Peter", 5)
        self.assertIsInstance(child, Person)
        self.assertEqual((child.name, child.age), ("Peter", 5))


if __name__ == "__main__":
    unittest.main()
