"""Testclass for highscore."""
import unittest
from unittest.mock import mock_open, patch
from PigDiceGame.highscore import Highscore


class TestHighscore(unittest.TestCase):
    """Test for highscore class."""

    def setUp(self):
        """Initialize setup for tests."""
        self.highscore = Highscore()

    def test_add_winner(self):
        """Method for adding winning."""
        self.highscore.add_winner("Player3")
        exp1 = {"Player3": 1}
        self.assertEqual(self.highscore.highscores, exp1)

        self.highscore.add_winner("Player4")
        exp2 = {"Player3": 1, "Player4": 1}
        self.assertEqual(self.highscore.highscores, exp2)

        self.highscore.add_winner("Player5")
        exp3 = {"Player3": 1, "Player4": 1, "Player5": 1}
        self.assertEqual(self.highscore.highscores, exp3)

    def test_sort_winners_score(self):
        """Test for sorting dictionary."""
        self.highscore.add_winner("Player1")
        self.highscore.add_winner("Player2")
        sorted_scores = self.highscore.sorted_list()
        exp = {"Player2": 1, "Player1": 1}
        self.assertEqual(sorted_scores, exp)

    def test_add_highscore(self):
        """Class method to test add highscore."""
        file_content = "Oliver : 20\nMarcus : 19\n"

        with patch("builtins.open", mock_open(read_data=file_content)):
            exp = {"Oliver": 20, "Marcus": 19}
            self.assertEqual(self.highscore.highscores, exp)

    def test_retreive_highscore(self):
        """Class method to test retreive highscore."""
        file_content = "Oliver : 20\nMarcus : 25\n"

        with patch("builtins.open", mock_open(read_data=file_content)):
            retrieved_highscores = self.highscore.retreive_highscore_file()

            exp = {"Oliver": 20, "Marcus": 25}
            self.assertEqual(retrieved_highscores, exp)


if __name__ == "__main__":
    unittest.main()
