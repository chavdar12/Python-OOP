import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Hero = runpy.run_path(str(Path(__file__).with_name("002_hero.py")))["Hero"]


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Peter", 100)

    def test_defend_survives(self):
        self.assertIsNone(self.hero.defend(50))
        self.assertEqual(self.hero.health, 50)

    def test_defend_defeated_clamps_to_zero(self):
        self.assertEqual(self.hero.defend(150), "Peter was defeated")
        self.assertEqual(self.hero.health, 0)

    def test_heal(self):
        self.hero.heal(50)
        self.assertEqual(self.hero.health, 150)


if __name__ == "__main__":
    unittest.main()
