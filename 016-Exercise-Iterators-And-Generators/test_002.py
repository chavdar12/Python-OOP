import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    dictionary_iter = runpy.run_path(str(Path(__file__).with_name("002.py")))["dictionary_iter"]


class TestDictionaryIter(unittest.TestCase):
    def test_yields_pairs(self):
        self.assertEqual(list(dictionary_iter({"name": "Peter", "age": 24})), [("name", "Peter"), ("age", 24)])

    def test_does_not_mutate_source(self):
        source = {1: "1", 2: "2"}
        list(dictionary_iter(source))
        self.assertEqual(source, {1: "1", 2: "2"})


if __name__ == "__main__":
    unittest.main()
