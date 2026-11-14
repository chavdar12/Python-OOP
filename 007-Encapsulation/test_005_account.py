import runpy
import unittest
from pathlib import Path

Account = runpy.run_path(str(Path(__file__).with_name("005_account.py")))["Account"]


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(8827312, 100, 3421)

    def test_get_id(self):
        self.assertEqual(self.account.get_id(111), "Wrong pin")
        self.assertEqual(self.account.get_id(3421), 8827312)

    def test_change_pin(self):
        self.assertEqual(self.account.change_pin(1, 2), "Wrong pin")
        self.assertEqual(self.account.change_pin(3421, 1234), "Pin changed")
        self.assertEqual(self.account.get_id(1234), 8827312)


if __name__ == "__main__":
    unittest.main()
