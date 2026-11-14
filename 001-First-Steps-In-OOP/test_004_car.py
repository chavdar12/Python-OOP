import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Car = runpy.run_path(str(Path(__file__).with_name("004_car.py")))["Car"]


class TestCar(unittest.TestCase):
    def test_get_info(self):
        self.assertEqual(Car("Kia", "Rio", "1.3L B3 I4").get_info(), "This is Kia Rio with engine 1.3L B3 I4")


if __name__ == "__main__":
    unittest.main()
