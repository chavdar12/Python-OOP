import unittest

from project.guild import Guild
from project.player import Player


class TestPlayer(unittest.TestCase):
    def test_add_skill(self):
        player = Player("George", 50, 100)
        self.assertEqual(player.add_skill("Shield Break", 20),
                         "Skill Shield Break added to the collection of the player George")
        self.assertEqual(player.add_skill("Shield Break", 20), "Skill already added")

    def test_player_info(self):
        player = Player("George", 50, 100)
        player.add_skill("Shield Break", 20)
        self.assertEqual(player.player_info(),
                         "Name: George\nGuild: Unaffiliated\nHP: 50\nMP: 100\n===Shield Break - 20")


class TestGuild(unittest.TestCase):
    def setUp(self):
        self.guild = Guild("UGT")
        self.player = Player("George", 50, 100)

    def test_assign_player(self):
        self.assertEqual(self.guild.assign_player(self.player), "Welcome player George to the guild UGT")
        self.assertEqual(self.player.guild, "UGT")
        self.assertEqual(self.guild.assign_player(self.player), "Player George is already in the guild.")
        self.assertEqual(Guild("Other").assign_player(self.player), "Player George is in another guild.")

    def test_kick_player(self):
        self.guild.assign_player(self.player)
        self.assertEqual(self.guild.kick_player("George"), "Player George has been removed from the guild.")
        self.assertEqual(self.player.guild, "Unaffiliated")
        self.assertEqual(self.guild.kick_player("George"), "Player George is not in the guild.")

    def test_guild_info(self):
        self.guild.assign_player(self.player)
        self.assertEqual(self.guild.guild_info(), "Guild: UGT\nName: George\nGuild: UGT\nHP: 50\nMP: 100\n")


if __name__ == "__main__":
    unittest.main()
