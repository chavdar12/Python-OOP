import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    get_primes = runpy.run_path(str(Path(__file__).with_name("008_prime_numbers.py")))["get_primes"]


class TestGetPrimes(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])), [2, 3, 5])
        self.assertEqual(list(get_primes([-2, 0, 0, 1, 1, 0])), [])


if __name__ == "__main__":
    unittest.main()
