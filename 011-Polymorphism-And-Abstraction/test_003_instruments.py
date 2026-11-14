import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("003_instruments.py")))


class TestStartPlaying(unittest.TestCase):
    def test_duck_typing(self):
        self.assertEqual(ns["start_playing"](ns["Guitar"]()), "Playing the guitar")
        self.assertEqual(ns["start_playing"](ns["Children"]()), "Children are playing")


if __name__ == "__main__":
    unittest.main()
