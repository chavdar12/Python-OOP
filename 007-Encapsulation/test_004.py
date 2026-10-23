import runpy
import unittest
from pathlib import Path

EmailValidator = runpy.run_path(str(Path(__file__).with_name("004.py")))["EmailValidator"]


class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator(6, ["gmail", "softuni"], ["com", "bg"])

    def test_valid(self):
        self.assertTrue(self.validator.validate("pe77er@gmail.com"))

    def test_invalid(self):
        self.assertFalse(self.validator.validate("georgios@gmail.net"))
        self.assertFalse(self.validator.validate("stamatito@abv.net"))
        self.assertFalse(self.validator.validate("abv@softuni.bg"))

    def test_multi_dot_domain_does_not_crash(self):
        self.assertFalse(self.validator.validate("peter123@gmail.co.uk"))


if __name__ == "__main__":
    unittest.main()
