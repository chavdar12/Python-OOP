import unittest

from project.blade_knight import BladeKnight
from project.dark_knight import DarkKnight
from project.dark_wizard import DarkWizard
from project.elf import Elf
from project.hero import Hero
from project.knight import Knight
from project.muse_elf import MuseElf
from project.soul_master import SoulMaster
from project.wizard import Wizard


class TestHeroes(unittest.TestCase):
    def test_parents(self):
        expected = {Elf: Hero, MuseElf: Elf, Wizard: Hero, DarkWizard: Wizard, SoulMaster: DarkWizard,
                    Knight: Hero, DarkKnight: Knight, BladeKnight: DarkKnight}
        for cls, parent in expected.items():
            with self.subTest(cls=cls.__name__):
                self.assertIs(cls.__bases__[0], parent)

    def test_str_uses_concrete_class_name(self):
        self.assertEqual(str(Hero("H", 4)), "H of type Hero has level 4")
        self.assertEqual(str(SoulMaster("SM", 99)), "SM of type SoulMaster has level 99")
        self.assertEqual(str(BladeKnight("blade", 8)), "blade of type BladeKnight has level 8")


if __name__ == "__main__":
    unittest.main()
