import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("005.py")))


class TestCache(unittest.TestCase):
    def test_cache_log(self):
        fibonacci = ns["cache"](lambda n: n * 2)
        self.assertEqual(fibonacci(3), 6)
        self.assertEqual(fibonacci.log, {3: 6})

    def test_fibonacci_is_memoized(self):
        self.assertEqual(ns["fibonacci"](10), 55)
        self.assertEqual(ns["fibonacci"].log[4], 3)


if __name__ == "__main__":
    unittest.main()
