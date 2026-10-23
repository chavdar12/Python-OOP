import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("ducks.py")))


class TestDucks(unittest.TestCase):
    def test_quack(self):
        self.assertEqual(ns["RubberDuck"].quack(), "Squeek")
        self.assertEqual(ns["RobotDuck"].quack(), "Robotic quacking")
        self.assertEqual(ns["RobotDuck"].walk(), "Robotic walking")

    def test_robot_lands_at_max_height(self):
        duck = ns["RobotDuck"]()
        for _ in range(ns["RobotDuck"].HEIGHT):
            duck.fly()
        self.assertEqual(duck.height, 50)
        duck.fly()
        self.assertEqual(duck.height, 0)

    def test_duck_is_abstract(self):
        with self.assertRaises(TypeError):
            ns["Duck"]()


if __name__ == "__main__":
    unittest.main()
