import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ImageArea = runpy.run_path(str(Path(__file__).with_name("002_image_area.py")))["ImageArea"]


class TestImageArea(unittest.TestCase):
    def test_comparisons_use_area(self):
        a1, a2, a3 = ImageArea(7, 10), ImageArea(35, 2), ImageArea(8, 9)
        self.assertTrue(a1 == a2)
        self.assertFalse(a1 != a2)
        self.assertTrue(a1 != a3)
        self.assertFalse(a1 >= a3)
        self.assertTrue(a1 <= a2)
        self.assertTrue(a1 < a3)
        self.assertTrue(a3 > a1)


if __name__ == "__main__":
    unittest.main()
