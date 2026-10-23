import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    vowels = runpy.run_path(str(Path(__file__).with_name("003.py")))["vowels"]


class TestVowels(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(list(vowels("Abcedifuty0o")), ["A", "e", "i", "u", "y", "o"])
        self.assertEqual(list(vowels("")), [])


if __name__ == "__main__":
    unittest.main()
