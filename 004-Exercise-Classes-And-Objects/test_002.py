import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Time = runpy.run_path(str(Path(__file__).with_name("002.py")))["Time"]


class TestTime(unittest.TestCase):
    def test_next_second(self):
        self.assertEqual(Time(9, 30, 58).next_second(), "09:30:59")
        self.assertEqual(Time(9, 30, 59).next_second(), "09:31:00")
        self.assertEqual(Time(10, 59, 59).next_second(), "11:00:00")
        self.assertEqual(Time(23, 59, 59).next_second(), "00:00:00")

    def test_set_time(self):
        time = Time(1, 2, 3)
        time.set_time(4, 5, 6)
        self.assertEqual(time.get_time(), "04:05:06")


if __name__ == "__main__":
    unittest.main()
