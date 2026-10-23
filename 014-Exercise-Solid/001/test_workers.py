import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(Path(__file__).with_name("workers.py")))


class TestManager(unittest.TestCase):
    def manage(self, worker):
        manager = ns["Manager"]()
        manager.set_worker(worker)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            manager.manage()
        return out.getvalue()

    def test_manages_every_worker_type(self):
        self.assertEqual(self.manage(ns["Worker"]()), "I'm working!!\n")
        self.assertEqual(self.manage(ns["SuperWorker"]()), "I work very hard!!!\n")
        self.assertEqual(self.manage(ns["LazyWorker"]()), "Working is not something I love doing...\n")

    def test_rejects_non_worker(self):
        with self.assertRaises(AssertionError):
            ns["Manager"]().set_worker(object())


if __name__ == "__main__":
    unittest.main()
