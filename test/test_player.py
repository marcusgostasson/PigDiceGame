import unittest
from PigDiceGame import Player


class test_Player(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        name = "bob"

        res = Player.Player(name)
        exp = Player.Player
        self.assertIsInstance(res, exp)

        playername = res.getName()
        self.assertEqual(playername, "bob")

    def test_throwdice(self):
        """Test if we get a random number between 1-6."""

        name = "bob"
        player = Player.Player(name)

        res = player.throwdice()
        exp = 1 <= res <= 6
        self.assertTrue(res, exp)
        
if __name__ == "__main__":
    unittest.main()
