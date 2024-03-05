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
        with patch('PigDiceGame.highscore.Highscore.add_highscore_to_file') as mock:
            self.highscore.add_winner("Player3")
            self.assertIn("Player3", self.highscore.highscores)

            self.highscore.add_winner("Player3")
            exp2 = {"Player3": 2}
            self.assertEqual(self.highscore.highscores, exp2)

            self.highscore.add_winner("Player5")
            exp3 = {"Player3": 2, "Player5": 1}
            self.assertEqual(self.highscore.highscores, exp3)

    def test_sort_winners_score(self):
        """Test for sorting dictionary."""
        with patch('PigDiceGame.highscore.Highscore.add_highscore_to_file') as mock:
            self.highscore.add_winner("Player1")
            self.highscore.add_winner("Player2")
            sorted_scores = {"Player1": 1, "Player2": 1}
            exp = {"Player1": 1, "Player2": 1}
            self.assertEqual(sorted_scores, exp)

    def test_add_highscore(self):
        """Class method to test add highscore."""
        file_content = "Oliver : 20\nMarcus : 19\n"

        with patch("builtins.open", mock_open(read_data=file_content)):
            exp = {"Oliver": 20, "Marcus": 19}
            self.assertEqual(file_content, exp)

    def test_retreive_highscore(self):
        """Class method to test retreive highscore."""
        file_content = "Oliver: 20\nMarcus: 25\n"

        with patch("builtins.open", mock_open(read_data=file_content)):
            retrieved_highscores = self.highscore.retreive_highscore_file()

            exp = {"Oliver": 20, "Marcus": 25}
            self.assertEqual(retrieved_highscores, exp)

    def test_get_name_and_highscore(self):
        """Class method to test get name and highscore."""
        self.highscore.sorted_list = lambda: [("Oliver", 10),
                                              ("Marcus", 12)]

        names, values = self.highscore.get_name_and_highscore()
        self.assertEqual(names, ["Oliver", "Marcus"])
        self.assertEqual(values, [10, 12])

if __name__ == "__main__":
    unittest.main()
