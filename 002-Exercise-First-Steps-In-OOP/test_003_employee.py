import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Employee = runpy.run_path(str(Path(__file__).with_name("003_employee.py")))["Employee"]


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(744423129, "John", "Smith", 1000)

    def test_full_name(self):
        self.assertEqual(self.employee.get_full_name(), "John Smith")

    def test_raise_and_annual_salary(self):
        self.assertEqual(self.employee.raise_salary(500), 1500)
        self.assertEqual(self.employee.get_annual_salary(), 18000)


if __name__ == "__main__":
    unittest.main()
