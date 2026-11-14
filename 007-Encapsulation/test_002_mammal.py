import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Mammal = runpy.run_path(str(Path(__file__).with_name("002_mammal.py")))["Mammal"]


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Dog", "Domestic", "Bark")

    def test_methods(self):
        self.assertEqual(self.mammal.make_sound(), "Dog makes Bark")
        self.assertEqual(self.mammal.get_kingdom(), "animals")
        self.assertEqual(self.mammal.info(), "Dog is of type Domestic")


if __name__ == "__main__":
    unittest.main()
