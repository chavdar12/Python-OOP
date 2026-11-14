import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Person = runpy.run_path(str(Path(__file__).with_name("001_person.py")))["Person"]


class TestPerson(unittest.TestCase):
    def test_getters(self):
        person = Person("George", 32)
        self.assertEqual((person.get_name(), person.get_age()), ("George", 32))

    def test_attributes_are_private(self):
        self.assertFalse(hasattr(Person("George", 32), "__name"))


if __name__ == "__main__":
    unittest.main()
