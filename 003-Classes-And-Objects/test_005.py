import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Smartphone = runpy.run_path(str(Path(__file__).with_name("005.py")))["Smartphone"]


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.phone = Smartphone(100)

    def test_install_when_off(self):
        self.assertEqual(self.phone.install("Facebook", 60), "Turn on your phone to install Facebook")

    def test_power_toggles(self):
        self.phone.power()
        self.assertTrue(self.phone.is_on)
        self.phone.power()
        self.assertFalse(self.phone.is_on)

    def test_install(self):
        self.phone.power()
        self.assertEqual(self.phone.install("Facebook", 60), "Installing Facebook")
        self.assertEqual(self.phone.install("Instagram", 60), "Not enough memory to install Instagram")
        self.assertEqual(self.phone.status(), "Total apps: 1. Memory left: 40")


if __name__ == "__main__":
    unittest.main()
