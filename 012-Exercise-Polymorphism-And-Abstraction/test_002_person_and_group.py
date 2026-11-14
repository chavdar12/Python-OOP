import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("002_person_and_group.py")))
Person, Group = ns["Person"], ns["Group"]


class TestPersonAndGroup(unittest.TestCase):
    def setUp(self):
        self.p2, self.p3 = Person("Warren", "Buffet"), Person("Elon", "Musk")

    def test_person_add(self):
        self.assertEqual(repr(self.p2 + self.p3), "Warren Musk")

    def test_group(self):
        first = Group("__VIP__", [self.p2])
        second = Group("Special", [self.p3])
        merged = first + second
        self.assertEqual(len(merged), 2)
        self.assertEqual(repr(merged), "Group __VIP__ Special with members Warren Buffet, Elon Musk")
        self.assertEqual(merged[1], "Person 1: Elon Musk")
        self.assertEqual(list(merged), ["Person 0: Warren Buffet", "Person 1: Elon Musk"])


if __name__ == "__main__":
    unittest.main()
