import contextlib
import io
import runpy
import unittest
from pathlib import Path

HERE = Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    books = runpy.run_path(str(HERE / "books.py"))
original_book = runpy.run_path(str(HERE / "books(original).py"))["Book"]


class TestBooks(unittest.TestCase):
    def test_turn_page(self):
        for book in (books["Book"]("T", "A"), original_book("T", "A", "shelf")):
            with self.subTest(book=book):
                book.turn_page(5)
                self.assertEqual(book.page, 5)

    def test_library_find_book(self):
        library = books["Library"]([books["Book"]("Svejk", "Hasek")])
        self.assertEqual(library.find_book("Svejk"), "Svejk, written by Hasek")
        self.assertIsNone(library.find_book("Missing"))


if __name__ == "__main__":
    unittest.main()
