"""Testclass for Player."""
import unittest
import sys
import os
from PigDiceGame.player import Player
from PigDiceGame.dice import Dice
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestPlayer(unittest.TestCase):
    """Test for the Player class."""

    def test_init_default_object(self):
        """Instantiate an object."""
        name = "Bob"

        res = Player(name)
        exp = Player
        self.assertIsInstance(res, exp)

    def test_get_name(self):
        """Test to see if i get a name correctly."""
        player = Player("Alice")

        res = player.get_name
        exp = "Alice"
        self.assertEqual(res, exp)

    def test_get_total_score(self):
        """Test to see if i get the total score correctly."""
        player = Player("Anna")

        res = player.get_total_score
        exp = 0
        self.assertEqual(res, exp)

    def test_get_tossed_amount(self):
        """Test to see if i get the tossed amount correctly."""
        player = Player("Klara")

        res = player.get_tossed_amount
        exp = 0
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Test to see if the name is set correctly."""
        player = Player("Nils")

        player.set_name("Olof")

        res = player.get_name()
        exp = "Olof"
        self.assertEqual(res, exp)

    def test_set_total_score(self):
        """Test to see if i can set the total_score."""
        player = Player("Mohammed")

        player.set_total_score(100)

        res = player.get_total_score()
        exp = 100
        self.assertEqual(res, exp)

    def test_throw_dice(self):
        """Test if throw_dice returns a valid random
        number and increments tossed amount."""

        player = Player("Peter")
        dice = Dice()

        res = player.throw_dice(dice)
        exp = 1 <= res <= 6
        self.assertTrue(res, exp)
        self.assertEqual(player.get_tossed_amount(), 1)


if __name__ == "__main__":
    unittest.main()
