import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Book = runpy.run_path(str(Path(__file__).with_name("003.py")))["Book"]


class TestBook(unittest.TestCase):
    def test_init(self):
        book = Book("My Book", "Me", 200)
        self.assertEqual((book.name, book.author, book.pages), ("My Book", "Me", 200))


if __name__ == "__main__":
    unittest.main()
