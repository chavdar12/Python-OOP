import contextlib
import io
import runpy
import unittest
from pathlib import Path


class TestScope(unittest.TestCase):
    def test_output(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            runpy.run_path(str(Path(__file__).with_name("002.py")))
        self.assertEqual(out.getvalue().splitlines(),
                         ["global", "outer: local", "inner: nonlocal", "outer: nonlocal", "global: changed!"])


if __name__ == "__main__":
    unittest.main()
