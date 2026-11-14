import unittest

from project.album import Album
from project.band import Band
from project.song import Song


class TestSong(unittest.TestCase):
    def test_get_info(self):
        self.assertEqual(Song("Running in the 90s", 3.45, False).get_info(), "Running in the 90s - 3.45")


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.song = Song("A", 3.15, False)
        self.album = Album("Initial D", self.song)

    def test_add_song(self):
        self.assertEqual(self.album.add_song(Song("B", 2.0, False)), "Song B has been added to the album Initial D.")
        self.assertEqual(self.album.add_song(Song("A", 1.0, False)), "Song is already in the album.")
        self.assertEqual(self.album.add_song(Song("S", 1.0, True)), "Cannot add S. It's a single")

    def test_remove_song(self):
        self.assertEqual(self.album.remove_song("A"), "Removed song A from album Initial D.")
        self.assertEqual(self.album.remove_song("A"), "Song is not in the album.")

    def test_publish_locks_album(self):
        self.assertEqual(self.album.publish(), "Album Initial D has been published.")
        self.assertEqual(self.album.publish(), "Album Initial D is already published.")
        self.assertEqual(self.album.add_song(Song("B", 2.0, False)), "Cannot add songs. Album is published.")
        self.assertEqual(self.album.remove_song("A"), "Cannot remove songs. Album is published.")

    def test_details(self):
        self.assertEqual(self.album.details(), "Album Initial D\n== A - 3.15")


class TestBand(unittest.TestCase):
    def setUp(self):
        self.band = Band("Death")
        self.album = Album("Perseverance")

    def test_add_album(self):
        self.assertEqual(self.band.add_album(self.album), "Band Death has added their newest album Perseverance.")
        self.assertEqual(self.band.add_album(self.album), "Band Death already has Perseverance in their library.")

    def test_remove_album(self):
        self.band.add_album(self.album)
        self.assertEqual(self.band.remove_album("Perseverance"), "Album Perseverance has been removed.")
        self.assertEqual(self.band.remove_album("Perseverance"), "Album Perseverance is not found.")

    def test_remove_published_album(self):
        self.album.publish()
        self.band.add_album(self.album)
        self.assertEqual(self.band.remove_album("Perseverance"), "Album has been published. It cannot be removed.")

    def test_details(self):
        self.band.add_album(self.album)
        self.assertEqual(self.band.details(), "Band Death\nAlbum Perseverance")


if __name__ == "__main__":
    unittest.main()
