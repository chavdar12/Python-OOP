import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    reverse_text = runpy.run_path(str(Path(__file__).with_name("006_reverse_string.py")))["reverse_text"]


class TestReverseText(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual("".join(reverse_text("step")), "pets")


if __name__ == "__main__":
    unittest.main()
