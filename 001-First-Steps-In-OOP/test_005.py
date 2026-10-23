import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Music = runpy.run_path(str(Path(__file__).with_name("005.py")))["Music"]


class TestMusic(unittest.TestCase):
    def setUp(self):
        self.song = Music("Title", "Artist", "Lyrics")

    def test_print_info(self):
        self.assertEqual(self.song.print_info(), 'This is "Title" from "Artist"')

    def test_play(self):
        self.assertEqual(self.song.play(), "Lyrics")


if __name__ == "__main__":
    unittest.main()
