import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("001.py")))


class TestRobots(unittest.TestCase):
    def test_sensors_amount(self):
        expected = {"Robot": 1, "MedicalRobot": 6, "ChefRobot": 4, "WarRobot": 12}
        for name, amount in expected.items():
            with self.subTest(robot=name):
                self.assertEqual(ns[name]("x").sensors_amount(), amount)

    def test_number_of_robot_sensors_prints(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ns["number_of_robot_sensors"](ns["WarRobot"]("Griffin"))
        self.assertEqual(out.getvalue(), "12\n")


if __name__ == "__main__":
    unittest.main()
