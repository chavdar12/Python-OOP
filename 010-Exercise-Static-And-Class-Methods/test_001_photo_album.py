import runpy
import unittest
from pathlib import Path

PhotoAlbum = runpy.run_path(str(Path(__file__).with_name("001_photo_album.py")))["PhotoAlbum"]


class TestPhotoAlbum(unittest.TestCase):
    def test_from_photos_count(self):
        self.assertEqual(PhotoAlbum.from_photos_count(5).pages, 2)
        self.assertEqual(PhotoAlbum.from_photos_count(4).pages, 1)

    def test_add_photo_fills_pages_in_order(self):
        album = PhotoAlbum(2)
        messages = [album.add_photo(f"p{i}") for i in range(1, 6)]
        self.assertEqual(messages[0], "p1 photo added successfully on page 1 slot 1")
        self.assertEqual(messages[3], "p4 photo added successfully on page 1 slot 4")
        self.assertEqual(messages[4], "p5 photo added successfully on page 2 slot 1")

    def test_album_full(self):
        album = PhotoAlbum(1)
        for i in range(4):
            album.add_photo(str(i))
        self.assertEqual(album.add_photo("extra"), "No more free slots")

    def test_display(self):
        album = PhotoAlbum(2)
        for i in range(5):
            album.add_photo(str(i))
        self.assertEqual(album.display(), "-----------\n[] [] [] []\n-----------\n[]\n-----------")


if __name__ == "__main__":
    unittest.main()
