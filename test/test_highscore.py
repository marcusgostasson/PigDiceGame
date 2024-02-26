import unittest
from PigDiceGame.highscore import Highscore

class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.highscores = Highscore()
        self.highscores.add_winner("Player1", 2)
        self.highscores.add_winner("Player2", 4)

    def test_add_winner(self):
        self.assertEqual(self.highscores.highscores, {"Player1": 2, "Player2": 4})

    def test_increase_score(self):
        self.highscores.increase_score("Player1")
        self.assertEqual(self.highscores.highscores["Player1"], 3)

    def test_sort_winners_score(self):
        sorted_scores = self.highscores.sort_winners_score()
        self.assertEqual(sorted_scores, {"Player2": 4, "Player1": 2})

    def test_sort_winners_player(self):
        sorted_players = self.highscores.sort_winners_player()
        self.assertEqual(sorted_players, {"Player1": 2, "Player2": 4})
                
if __name__=="__main__":
    unittest.main()