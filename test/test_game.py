#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
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

        exp = g.checkIfWinner(50)
        res = True
        self.assertEqual(exp, res)

    @patch("builtins.input", side_effect=["invalid", 1])
    def test_get_choice_from_user(self, mock_input):
        g = game.Game()
        choice = g.get_choice_from_user("Choice: ")
        self.assertIsNone(choice)

        choice = g.get_choice_from_user("Choice: ")
        self.assertEqual(choice, 1)


if __name__ == "__main__":
    unittest.main()
