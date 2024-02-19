#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game


class Test_game(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Game()
        self.assertIsInstance(res, game.Game)

    def test_check_Winner(self):
        g = game.Game()
        exp = g.checkIfWinner(100)
        res = False
        self.assertEqual(exp, res)


if __name__ == "__main__":
    unittest.main()
