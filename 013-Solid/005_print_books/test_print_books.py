import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("print_books.py")))


class TestPrinter(unittest.TestCase):
    def test_formatters(self):
        book = ns["Book"]("Lorem Ipsum")
        expected = {"RegularFormatter": "Lorem Ipsum", "UpperCaseFormatter": "LOREM IPSUM",
                    "LowerCaseFormatter": "lorem ipsum", "ReversingFormatter": "muspI meroL"}
        for formatter, text in expected.items():
            with self.subTest(formatter=formatter):
                self.assertEqual(ns["Printer"](ns[formatter]()).get_book(book), text)


if __name__ == "__main__":
    unittest.main()
