import unittest

from project.player import Player
from project.team import Team


class TestPlayer(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Player("Pall", 1, 3, 5, 7)),
                         "Player: Pall\nSprint: 1\nDribble: 3\nPassing: 5\nShooting: 7")


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Best", 10)
        self.player = Player("Pall", 1, 3, 5, 7)

    def test_add_player(self):
        self.assertEqual(self.team.add_player(self.player), "Player Pall joined team Best")
        self.assertEqual(self.team.add_player(self.player), "Player Pall has already joined")

    def test_remove_player(self):
        self.team.add_player(self.player)
        self.assertIs(self.team.remove_player("Pall"), self.player)
        self.assertEqual(self.team.remove_player("Pall"), "Player Pall not found")


if __name__ == "__main__":
    unittest.main()
