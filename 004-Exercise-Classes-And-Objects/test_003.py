import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Account = runpy.run_path(str(Path(__file__).with_name("003.py")))["Account"]


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(1234, "George", 1000)

    def test_credit(self):
        self.assertEqual(self.account.credit(500), 1500)

    def test_debit(self):
        self.assertEqual(self.account.debit(1500), "Amount exceeded balance")
        self.assertEqual(self.account.debit(1000), 0)

    def test_info(self):
        self.assertEqual(self.account.info(), "User George with account 1234 has 1000 balance")


if __name__ == "__main__":
    unittest.main()
