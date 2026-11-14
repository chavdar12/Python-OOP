import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("001_logged.py")))


class TestLogged(unittest.TestCase):
    def test_logged(self):
        self.assertEqual(ns["func"](4, 4, 4), "you called func(4, 4, 4)\nit returned 6")
        self.assertEqual(ns["sum_func"](1, 4), "you called sum_func(1, 4)\nit returned 5")


if __name__ == "__main__":
    unittest.main()
