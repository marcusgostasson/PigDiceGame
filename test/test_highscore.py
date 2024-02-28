"""Testclass for highscore."""
import unittest
from PigDiceGame.highscore import Highscore

class TestHighscore(unittest.TestCase):
    """Test for highscore class"""
    def setUp(self):
        self.highscore = Highscore()

    def test_add_winner(self):
        """"Test for adding winning"""
        self.highscore.add_winner("player1")
        exp = {"Player1": 1}
        self.assertEqual(self.highscore.highscores, exp)
        
        self.highscore.add_winner("Player2")
        exp = {"Player2": 1}
        self.assertEqual(self.highscore.highscores, exp)
        
        self.highscore.add_winner("Player1")
        exp = {"Player1": 2}
        self.assertEqual(self.highscore.highscores, exp)
        
        

    def test_increase_score(self):
        """Test for increasing score"""
        self.highscore.add_winner("Player1")
        self.highscore.increase_score("Player1")
        exp = {"Player1": 2}
        self.assertEqual(self.highscore.highscores, exp)

    def test_sort_winners_score(self):
        """Test for sorting dictionary"""
        self.highscore.add_winner("Player1")
        self.highscore.add_winner("Player2")
        sorted_scores = self.highscore.sort_winners_score()
        exp = {"Player2": 1, "Player1": 1}
        self.assertEqual(sorted_scores, exp)
                
if __name__=="__main__":
    unittest.main()