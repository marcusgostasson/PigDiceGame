import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PigDiceGame import game, player, computer


class Testgame(unittest.TestCase):
    """All the tests for the game class"""

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

    def test_check_winner_player(self):
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

    def test_check_if_winner_computer(self):
        """Checks if the output is correct when the computer wins
        and if the dictionary is updated correctly."""
        g = game.Game()
        c = computer.Computer("1")
        with patch("builtins.print") as mock_print:
            g.check_if_winner(100, c)
            mock_print.assert_any_call(game.GREEN + "Computer won in 0"
                                       + " throws!" + game.END)
        name, points = g.players.popitem()
        self.assertEqual(name, "Computer")
        self.assertEqual(points, 100)

    @patch("builtins.input", side_effect=["1", "word", "4"])
    def test_get_choice_from_user(self, mock_input):
        """Tests if choice from user is invalid for a string and valid for 1"""

        g = game.Game()

        choice = g.get_choice_from_user("Choice: ")
        self.assertEqual(choice, "1")
        p = player.Player("Sven")
        with patch("builtins.print") as mock_print:
            g.player_playing(p)
            mock_print.assert_any_call(game.RED + "That's not an option" + game.END)

    @patch("PigDiceGame.dice.Dice.get_random_number", return_value=2) # Die always roll 2
    @patch("builtins.input", side_effect=["1", "Bob", "raz", "1", "2", "4", "5"])
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
        """Testing if the setup works that the name is the same."""

        g = game.Game()
        player = g.setup_player()

        players_name = player.get_name()
        self.assertEqual(players_name, "Bob")

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_rules(self, mock_stdout):
        """Tests if the game rules prints out the same."""

        expected_output = """\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n"""

        game.Game().handle_choice("3")

        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    @patch("builtins.input", side_effect=["bob", "raz", "4"])
    def test_player_vs_player_p1_surrenders(self, mock_input):
        """Tests if the output is correct if the first player surrenders."""

        g = game.Game()
        with patch("builtins.print") as mock_print:
            g.player_vs_player()
            mock_print.assert_called_with(game.RED + "Bob" + " surrendered" + game.END + " and " + game.GREEN + "Raz" + " won" + game.END)

    @patch("builtins.input", side_effect=["bob", "raz", "2", "4", "4", "4"])
    def test_player_vs_player_p2_surrenders(self, mock_input):
        """Tests if the output is correct if the second player surrenders."""

        g = game.Game()
        with patch("builtins.print") as mock_print:
            g.player_vs_player()
            mock_print.assert_called_with(game.RED + "Raz" + " surrendered" + game.END + " and " + game.GREEN + "Bob" + " won" + game.END)

    def test_handle_choice_invalid(self):
        """Tests if an invalid option for handle_choice prints right output."""

        g = game.Game()
        with patch("builtins.print") as mock_print:
            g.handle_choice(6)
            mock_print.assert_called_with(game.RED + "Invalid option" + game.END)

    @patch("PigDiceGame.dice.Dice.get_random_number", return_value=1)
    @patch("builtins.input", side_effect=["1"])
    def test_player_playing_when_getting_a_one(self, mock_input, mock_choices):
        """Tests if the output is correct when the user gets a 1."""

        g = game.Game()
        p = player.Player("bob")

        with patch("builtins.print") as mock_print:
            g.player_playing(p)
            mock_print.assert_called_with("Oh you got a " + "1" + " better luck next time\n")

    @patch("builtins.input", side_effect=["3", "Sven", "4", "3", "Sven", "4", "4"])
    def test_user_press_3_change_name_prints_correct(self, mock_input):
        """Checks if the output is correct after the named is changed
        and that the dictionary is correct."""

        g = game.Game()
        p = player.Player("Bob")
        g.players["Bob"] = 0

        self.assertIn("Bob", g.players)
        g.player_playing(p)
        self.assertNotIn("Bob", g.players)
        self.assertIn("Sven", g.players)

        with patch("builtins.print") as mock_print:
            g.player_playing(p)
            mock_print.assert_any_call("Your new name is now Sven")

    @patch("builtins.input", side_effect=["ezwin"])
    def test_player_cheats(self, mock_input):
        """Testing if the cheats work that the player gets 100 points."""
        g = game.Game()
        p = player.Player("Bob")
        g.players["Bob"] = 0
        g.player_playing(p)

        max_points = g.get_player_score("Bob")
        self.assertEqual(max_points, 100)

    def test_get_player_score_when_none(self):
        """Tests if the get_player_score returns None if the name does
        not exist in the dictionary."""
        g = game.Game()
        empty = g.get_player_score("Bob")
        self.assertEqual(empty, None)

    @patch("builtins.input", side_effect=["12", "4"])
    def test_player_playing_invalid_input(self, mock_input):
        """Testsing the player_playing when invalid input 12 in this case."""
        g = game.Game()
        p = player.Player("Bob")
        with patch("builtins.print") as mock_print:
            g.player_playing(p)
            mock_print.assert_any_call(game.RED + "That's not an option" + game.END)

    @patch("PigDiceGame.dice.Dice.get_random_number", return_value=6)
    @patch("builtins.input", side_effect=["Raz", "1", "2", "4"])
    def test_player_vs_computer(self, mock_input, mock_choice):
        """Testing the player vs computer function."""

        g = game.Game()
        g.player_vs_computer()
        self.assertIn("Raz", g.players)
        self.assertIn("Computer", g.players)

    @patch("PigDiceGame.dice.Dice.get_random_number", return_value=1)
    def test_computer_playing_when_get_1(self, mock_choice):
        """Testing if the output is right when the computer rolls a 1."""
        g = game.Game()
        c = computer.Computer("1")
        with patch("builtins.print") as mock_print:
            g.computer_playing(c)
            mock_print.assert_any_call("Oh you got a 1"
                                       + " better luck next time\n")


if __name__ == "__main__":
    unittest.main()
