import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("004_type_check.py")))


class TestTypeCheck(unittest.TestCase):
    def test_type_check(self):
        self.assertEqual(ns["times2"](2), 4)
        self.assertEqual(ns["times2"]("Not A Number"), "Bad Type")
        self.assertEqual(ns["first_letter"]("Hello World"), "H")
        self.assertEqual(ns["first_letter"](["Not", "A", "String"]), "Bad Type")


if __name__ == "__main__":
    unittest.main()
