import runpy
import unittest
from pathlib import Path

ns = runpy.run_path(str(Path(__file__).with_name("003_command.py")))


class TestCommand(unittest.TestCase):
    def test_invokers_run_their_command(self):
        save = ns["SaveCommand"](ns["Document"]("notes.txt"))
        exit_ = ns["ExitCommand"](ns["Window"]())
        self.assertEqual(ns["ToolbarDocument"](save).click(), "notes.txt saved")
        self.assertEqual(ns["MenuItem"](exit_).click(), "Window closed")
        self.assertEqual(ns["KeyboardShortcut"](save).keypress(), "notes.txt saved")


if __name__ == "__main__":
    unittest.main()
