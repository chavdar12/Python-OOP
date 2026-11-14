import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Programmer = runpy.run_path(str(Path(__file__).with_name("007_programmer.py")))["Programmer"]


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer("John", "Java", 50)

    def test_watch_course(self):
        self.assertEqual(self.programmer.watch_course("Py", "Python", 84), "John does not know Python")
        self.assertEqual(self.programmer.watch_course("J", "Java", 50), "John watched J")
        self.assertEqual(self.programmer.skills, 100)

    def test_change_language(self):
        self.assertEqual(self.programmer.change_language("Java", 30), "John already knows Java")
        self.assertEqual(self.programmer.change_language("Python", 100), "John needs 50 more skills")
        self.assertEqual(self.programmer.change_language("Python", 50), "John switched from Java to Python")
        self.assertEqual(self.programmer.language, "Python")


if __name__ == "__main__":
    unittest.main()
