import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Shop = runpy.run_path(str(Path(__file__).with_name("001.py")))["Shop"]


class TestShop(unittest.TestCase):
    def test_items_count(self):
        self.assertEqual(Shop("My Shop", ["Apples", "Bananas", "Cucumbers"]).get_items_count(), 3)
        self.assertEqual(Shop("Empty", []).get_items_count(), 0)


if __name__ == "__main__":
    unittest.main()
