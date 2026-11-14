import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest import mock

# the module times a 10M-iteration loop on import; shrink it so the test stays fast
with mock.patch("builtins.range", lambda *args: iter(())), contextlib.redirect_stdout(io.StringIO()):
    exec_time = runpy.run_path(str(Path(__file__).with_name("007_execution_time.py")))["exec_time"]


class TestExecTime(unittest.TestCase):
    def test_returns_elapsed_seconds(self):
        elapsed = exec_time(lambda: sum(range(1000)))()
        self.assertIsInstance(elapsed, float)
        self.assertGreaterEqual(elapsed, 0)


if __name__ == "__main__":
    unittest.main()
