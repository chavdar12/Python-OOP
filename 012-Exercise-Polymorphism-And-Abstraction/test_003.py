import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Account = runpy.run_path(str(Path(__file__).with_name("003.py")))["Account"]


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.acc = Account("bob", 10)
        for amount in (20, -20, 30):
            self.acc.add_transaction(amount)

    def test_str_and_repr(self):
        self.assertEqual(str(self.acc), "Account of bob with starting amount: 10")
        self.assertEqual(repr(self.acc), "Account(bob, 10)")

    def test_transactions(self):
        self.assertEqual(self.acc.balance, 40)
        self.assertEqual(len(self.acc), 3)
        self.assertEqual(self.acc[1], -20)
        self.assertEqual(list(reversed(self.acc)), [30, -20, 20])

    def test_add_transaction_rejects_non_int(self):
        with self.assertRaises(ValueError):
            self.acc.add_transaction(1.5)

    def test_validate_transaction(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.acc, -100)
        self.assertEqual(Account.validate_transaction(self.acc, 10), "New balance: 50")

    def test_comparisons_and_add(self):
        other = Account("john")
        other.add_transaction(70)
        self.assertTrue(self.acc < other)
        self.assertFalse(self.acc == other)
        merged = self.acc + other
        self.assertEqual(str(merged), "Account of bob&john with starting amount: 10")
        self.assertEqual(merged.balance, 110)


if __name__ == "__main__":
    unittest.main()
