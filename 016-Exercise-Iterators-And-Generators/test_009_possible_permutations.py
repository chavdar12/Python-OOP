import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    possible_permutations = runpy.run_path(str(Path(__file__).with_name("009_possible_permutations.py")))["possible_permutations"]


class TestPossiblePermutations(unittest.TestCase):
    def test_permutations(self):
        self.assertEqual(list(possible_permutations([1, 2, 3])),
                         [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        self.assertEqual(list(possible_permutations([1])), [[1]])


if __name__ == "__main__":
    unittest.main()
