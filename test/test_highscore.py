import unittest
from PigDiceGame.highscore import Highscore

class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.highscore = Highscore()

    def test_add_winner(self):
        self.highscore.add_winner("player1")
        self.assertEqual(self.highscore.highscores["Player1"], 0)
        
        self.highscore.add_winner("Player2")
        self.assertEqual(self.highscore.highscores["Player2"], 0)
        
        self.highscore.add_winner("Player1")
        self.assertEqual(self.highscore.highscores["Player1"], 1)
        

    def test_increase_score(self):
        self.highscore.increase_score("Player1")
        self.assertEqual(self.highscore.highscores["Player1"], 2)

    def test_sort_winners_score(self):
        sorted_scores = self.highscore.sort_winners_score()
        exp = {"Player2": 0, "Player1": 2}
        self.assertEqual(sorted_scores, exp)
                
if __name__=="__main__":
    unittest.main()