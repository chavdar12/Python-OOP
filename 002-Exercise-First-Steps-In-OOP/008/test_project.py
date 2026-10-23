import unittest

from project.pokemon import Pokemon
from project.trainer import Trainer


class TestPokemon(unittest.TestCase):
    def test_details(self):
        self.assertEqual(Pokemon("Pikachu", 90).pokemon_details(), "Pikachu with health 90")


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.trainer = Trainer("Ash")
        self.pikachu = Pokemon("Pikachu", 90)

    def test_add_pokemon(self):
        self.assertEqual(self.trainer.add_pokemon(self.pikachu), "Caught Pikachu with health 90")
        self.assertEqual(self.trainer.add_pokemon(self.pikachu), "This pokemon is already caught")
        self.assertEqual(len(self.trainer.pokemons), 1)

    def test_release_pokemon(self):
        self.trainer.add_pokemon(self.pikachu)
        self.assertEqual(self.trainer.release_pokemon("Pikachu"), "You have released Pikachu")
        self.assertEqual(self.trainer.release_pokemon("Pikachu"), "Pokemon is not caught")

    def test_trainer_data(self):
        self.trainer.add_pokemon(self.pikachu)
        self.trainer.add_pokemon(Pokemon("Charizard", 110))
        self.assertEqual(self.trainer.trainer_data(),
                         "Pokemon Trainer Ash\nPokemon count 2\n- Pikachu with health 90\n- Charizard with health 110")


if __name__ == "__main__":
    unittest.main()
