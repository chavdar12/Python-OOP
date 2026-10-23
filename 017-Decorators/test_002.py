import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("002.py")))


class TestVowelFilter(unittest.TestCase):
    def test_filters_vowels(self):
        self.assertEqual(ns["get_letters"](), ["a", "e"])
        self.assertEqual(ns["vowel_filter"](lambda: list("Python"))(), ["y", "o"])


if __name__ == "__main__":
    unittest.main()
