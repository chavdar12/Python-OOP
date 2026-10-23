import runpy
import unittest
from pathlib import Path

Profile = runpy.run_path(str(Path(__file__).with_name("003.py")))["Profile"]
PASSWORD_ERROR = "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."


class TestProfile(unittest.TestCase):
    def test_valid_profile(self):
        self.assertEqual(str(Profile("Username", "Passw0rd")),
                         'You have a profile with username: "Username" and password: ********')

    def test_invalid_username(self):
        for name in ["abcd", "a" * 16]:
            with self.subTest(name=name), self.assertRaises(ValueError) as ctx:
                Profile(name, "Passw0rd")
            self.assertEqual(str(ctx.exception), "The username must be between 5 and 15 characters.")

    def test_invalid_password(self):
        for password in ["Pa0", "password1", "Password"]:
            with self.subTest(password=password), self.assertRaises(ValueError) as ctx:
                Profile("Username", password)
            self.assertEqual(str(ctx.exception), PASSWORD_ERROR)


if __name__ == "__main__":
    unittest.main()
