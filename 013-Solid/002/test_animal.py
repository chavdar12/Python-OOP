import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("animal.py")))


class TestAnimals(unittest.TestCase):
    def test_sound_and_species(self):
        for cls, sound, species in [("Cat", "meow", "cat"), ("Dog", "woof-woof", "dog"),
                                    ("Chicken", "chik-chirik", "chicken")]:
            with self.subTest(cls=cls):
                self.assertEqual((ns[cls]().get_sound(), ns[cls]().get_species()), (sound, species))

    def test_animal_sound_prints_each(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ns["animal_sound"]([ns["Cat"](), ns["Chicken"]()])
        self.assertEqual(out.getvalue(), "meow\nchik-chirik\n")


if __name__ == "__main__":
    unittest.main()
