import contextlib
import io
import runpy
import unittest
from pathlib import Path
from unittest import mock

with mock.patch("time.sleep"), contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("workers_updated.py")))


class TestManager(unittest.TestCase):
    def test_abstract_worker_is_enforced(self):
        with self.assertRaises(TypeError):
            ns["AbstractWorker"]()

    def test_lunch_break(self):
        manager = ns["Manager"]()
        manager.set_worker(ns["Robot"]())
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            manager.manage()
            manager.lunch_break()
        self.assertEqual(out.getvalue(), "I'm a robot. I'm working....\nI don't need to eat....\n")

    def test_worker_eats(self):
        out = io.StringIO()
        with mock.patch("time.sleep") as sleep, contextlib.redirect_stdout(out):
            ns["Worker"]().eat()
        sleep.assert_called_once_with(5)


if __name__ == "__main__":
    unittest.main()
