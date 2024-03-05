"""Testclass for highscore."""
import unittest
import tempfile
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
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            self.highscore.file_path = tmp_file.name

            self.highscore.add_highscore_to_file({})

            with open(tmp_file.name, 'r', encoding='utf-8') as file:
                actual_content = file.read()

        exp = ""
        self.assertEqual(actual_content, exp)

    def test_retreive_highscore(self):
        """Class method to test retreive highscore."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            self.highscore.file_path = tmp_file.name

            retreived_score = self.highscore.retreive_highscore_file()

        exp = {}
        self.assertEqual(retreived_score, exp)

    def test_get_name_and_highscore(self):
        """Class method to test get name and highscore."""
        self.highscore.sorted_list = lambda: [("Oliver", 10),
                                              ("Marcus", 12)]

        names, values = self.highscore.get_name_and_highscore()
        self.assertEqual(names, ["Oliver", "Marcus"])
        self.assertEqual(values, [10, 12])

if __name__ == "__main__":
    unittest.main()
