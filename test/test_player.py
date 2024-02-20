"""Testclass for Player"""
import unittest
from PigDiceGame.player import Player
from PigDiceGame.dice import Dice


class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        name = "Bob"

        res = Player(name)
        exp = Player
        self.assertIsInstance(res, exp)

        playername = res.get_name()
        self.assertEqual(playername, "Bob")

    def test_throw_dice_success(self):
        """
        Test if throw_dice returns a valid random
        number and increments tossed amount.
        """
        player = Player("Alice")
        dice = Dice()

        res = player.throw_dice(dice)
        exp = 1 <= res <= 6
        self.assertTrue(res, exp)
        self.assertEqual(player.get_tossed_amount(), 1)

if __name__ == "__main__":
    unittest.main()
