#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, player


class Test_game(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        g = game.Game()
        self.assertIsInstance(g, game.Game)

        players = g.players
        exp = {}
        self.assertEqual(players, exp)

        exp = g.playing
        res = True
        self.assertEqual(exp, res)

    def test_check_winner(self):
        """Checks if the player wins if he has 100 points and 
        checks if the player is still playing if he has 50 points"""
        g = game.Game()
        p = player.Player("Bob")
        exp = g.check_if_winner(100, p)
        res = False
        self.assertEqual(exp, res)

        exp = g.check_if_winner(50, p)
        res = True
        self.assertEqual(exp, res)

    @patch("builtins.input", side_effect=["hej", "1"])
    def test_get_choice_from_user(self, mock_input):
        """Tests if choice from user works for an invalid input and valid for 1"""
        g = game.Game()
        with self.assertRaises(ValueError):
            g.get_choice_from_user("Choice: ")

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

    @patch("builtins.input", side_effect=["bob", "sven"])
    def test_change_name(self, mock_input):
        """Testing to change name from bob to sven"""
        g = game.Game()
        p = player.Player("bob")
        bob = g.change_name(p)
        exp_new_name = g.change_name(p)

        self.assertEqual(exp_new_name, "sven")

    @patch("builtins.input", side_effect=["bob"])
    def test_setup_player(self, mock_input):
        g = game.Game()
        player = g.setup_player()

        players_name = player.get_name()
        self.assertEqual(players_name, "bob")

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_rules(self, mock_stdout):
        expected_output = """\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n"""

        game.Game().game_rules()

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
