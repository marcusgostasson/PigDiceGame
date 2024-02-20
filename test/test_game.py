#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import sys
import os
import io
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, player


class Test_game(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Game()
        self.assertIsInstance(res, game.Game)

    def test_check_winner(self):
        g = game.Game()
        p = player.Player("Bob")
        exp = g.check_if_winner(100, p)
        res = False
        self.assertEqual(exp, res)

        exp = g.check_if_winner(50, p)
        res = True
        self.assertEqual(exp, res)

    @patch("builtins.input", side_effect=["invalid", "1"])
    def test_get_choice_from_user(self, mock_input):
        g = game.Game()
        choice = g.get_choice_from_user("Choice: ")
        self.assertIsNone(choice)

        choice = g.get_choice_from_user("Choice: ")
        self.assertEqual(choice, 1)

    @patch("PigDiceGame.dice.Dice.get_random_number", return_value=2) # Die always roll 2
    @patch("builtins.input", side_effect=["1", "Bob", "raz", "1", "2", "4", "4"])
    def test_start_game_with_choice_one_then_stay(self, mock_input, mock_choices):
        """Tests to start the game and let player1 roll then stay to see that the score is updated"""
        g = game.Game()
        g.start_game()

        player_score_before_toss = g.get_player_score("Bob")
        self.assertGreater(player_score_before_toss, 0)


if __name__ == "__main__":
    unittest.main()
