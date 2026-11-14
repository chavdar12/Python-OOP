import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    SteamUser = runpy.run_path(str(Path(__file__).with_name("006_steam_user.py")))["SteamUser"]


class TestSteamUser(unittest.TestCase):
    def setUp(self):
        self.user = SteamUser("Peter", ["CS:GO", "Fortnite"])

    def test_play_owned_game(self):
        self.assertEqual(self.user.play("Fortnite", 3), "Peter is playing Fortnite")
        self.assertEqual(self.user.played_hours, 3)

    def test_play_missing_game(self):
        self.assertEqual(self.user.play("Oxygen", 5), "Oxygen is not in library")
        self.assertEqual(self.user.played_hours, 0)

    def test_buy_game(self):
        self.assertEqual(self.user.buy_game("CS:GO"), "CS:GO is already in your library")
        self.assertEqual(self.user.buy_game("Oxygen"), "Peter bought Oxygen")
        self.assertIn("Oxygen", self.user.games)

    def test_status(self):
        self.user.play("CS:GO", 4)
        self.assertEqual(self.user.status(), "Peter has 2 games. Total play time: 4")


if __name__ == "__main__":
    unittest.main()
