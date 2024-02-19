#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from PigDiceGame import Game


class Test_Game(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game.Game()
        exp = Game.Game
        self.assertIsInstance(res, exp)

    def test_start_the_game(self):
        """Roll a dice and check value is in bounds."""
        the_game = Game.Game()
        the_game.start()

        res = the_game.the_number
        exp = the_game.low_number <= res <= the_game.high_number
        self.assertTrue(exp)

    def test_throwdice(self):
        """Test if we get a random number between 1-6."""
        player = Player.Player()

        res = player.throwdice()
        exp = 1 <= res <= 6
        self.assertTrue(res, exp)

if __name__ == "__main__":
    unittest.main()
