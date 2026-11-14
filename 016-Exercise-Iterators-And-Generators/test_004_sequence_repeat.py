import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    sequence_repeat = runpy.run_path(str(Path(__file__).with_name("004_sequence_repeat.py")))["sequence_repeat"]


class TestSequenceRepeat(unittest.TestCase):
    def test_repeat(self):
        self.assertEqual("".join(sequence_repeat("abc", 5)), "abcab")
        self.assertEqual("".join(sequence_repeat("I Love Python", 3)), "I L")


if __name__ == "__main__":
    unittest.main()
