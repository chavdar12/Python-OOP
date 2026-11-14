import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    countdown_iterator = runpy.run_path(str(Path(__file__).with_name("003_countdown_iterator.py")))["countdown_iterator"]


class TestCountdownIterator(unittest.TestCase):
    def test_countdown(self):
        self.assertEqual(list(countdown_iterator(10)), list(range(10, -1, -1)))
        self.assertEqual(list(countdown_iterator(0)), [0])


if __name__ == "__main__":
    unittest.main()
