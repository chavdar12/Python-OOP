import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    read_next = runpy.run_path(str(Path(__file__).with_name("007.py")))["read_next"]


class TestReadNext(unittest.TestCase):
    def test_reads_all_iterables(self):
        self.assertEqual("".join(map(str, read_next("string", (2,), {"d": 1, "I": 2}))), "string2dI")
        self.assertEqual(list(read_next("Ne", ["words"])), ["N", "e", "words"])


if __name__ == "__main__":
    unittest.main()
