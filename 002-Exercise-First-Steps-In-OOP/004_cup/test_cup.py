import contextlib
import io
import runpy
import unittest
from pathlib import Path


def load_cup(file_name):
    with contextlib.redirect_stdout(io.StringIO()):
        return runpy.run_path(str(Path(__file__).with_name(file_name)))["Cup"]


class CupTests:
    def test_status(self):
        self.assertEqual(self.Cup(100, 50).status(), 50)

    def test_fill_within_size(self):
        cup = self.Cup(100, 50)
        cup.fill(40)
        self.assertEqual(cup.status(), 10)

    def test_fill_overflow_is_ignored(self):
        cup = self.Cup(100, 50)
        cup.fill(60)
        self.assertEqual(cup.quantity, 50)

    def test_fill_exactly_to_size(self):
        cup = self.Cup(100, 50)
        cup.fill(50)
        self.assertEqual(cup.status(), 0)


class TestCup1(CupTests, unittest.TestCase):
    Cup = load_cup("cup_1.py")


class TestCup2(CupTests, unittest.TestCase):
    Cup = load_cup("cup_2.py")


if __name__ == "__main__":
    unittest.main()
