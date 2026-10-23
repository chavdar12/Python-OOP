import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("prisoner.py")))


class TestPrisoner(unittest.TestCase):
    def test_free_man_walks(self):
        free_man = ns["FreeMan"]([11, 11])
        free_man.walk_north(10)
        free_man.walk_east(-3)
        self.assertEqual(free_man.position, [8, 21])

    def test_prisoner_cannot_walk(self):
        prisoner = ns["Prisoner"]()
        self.assertFalse(hasattr(prisoner, "walk_north"))
        self.assertEqual(prisoner.position, [3, 3])
        self.assertIsNot(prisoner.position, ns["Prisoner"].PRISON_LOCATION)


if __name__ == "__main__":
    unittest.main()
