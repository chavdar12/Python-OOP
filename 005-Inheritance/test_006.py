import runpy
import unittest
from pathlib import Path

Stack = runpy.run_path(str(Path(__file__).with_name("006.py")))["Stack"]


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(str(self.stack), "[]")

    def test_push_pop_top(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.top(), "b")
        self.assertEqual(str(self.stack), "[b, a]")
        self.assertEqual(self.stack.pop(), "b")
        self.assertFalse(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()
