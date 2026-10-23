import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Glass = runpy.run_path(str(Path(__file__).with_name("004.py")))["Glass"]


class TestGlass(unittest.TestCase):
    def setUp(self):
        self.glass = Glass()

    def test_fill(self):
        self.assertEqual(self.glass.fill(100), "Glass filled with 100 ml")
        self.assertEqual(self.glass.fill(200), "Cannot add 200 ml")
        self.assertEqual(self.glass.info(), "150 ml left")

    def test_fill_to_capacity(self):
        self.assertEqual(self.glass.fill(250), "Glass filled with 250 ml")

    def test_empty(self):
        self.glass.fill(100)
        self.assertEqual(self.glass.empty(), "Glass is now empty")
        self.assertEqual(self.glass.info(), "250 ml left")


if __name__ == "__main__":
    unittest.main()
