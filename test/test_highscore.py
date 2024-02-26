import unittest
import os
import sys

from PigDiceGame.highscore import Highscore
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class test_highScore(unittest.TestCase):
    """Initiate highscore"""
    
    def setUp(self):
        self.highscores = highscore()
        self.test_file_path = "test_highscore_list.txt"
        
    def test_file_reset(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
            
    def test_content_written_to_file(self):
        """Test the contents written to file"""
        self.highscores.highscores = {"Oliver": 15, "Razmus": 14, "Emil": 16}
        
        self.highscores.seperate_highscores(file_path=self.test_file_path)
        
        with open(self.test_file_path, 'r') as file:
            file_content = file.read()
            
        exp = "Oliver : 15\nRazmus : 14\nEmil : 16\n"
        self.assertEqual(file_content, exp)

    def test_round_over(self):
        """Test with valid scores"""
        self.highscores.round_over("Oliver",10)
        self.assertEqual(self.highscores.highscores["Oliver"], 10)
        
        with self.assertRaises(ValueError):
            self.highscores.round_over(101, 10)
            
        with self.assertRaises(ValueError):
            self.highscores.round_over("Razmus", -5)
            
    def test_file_format(self):
        """Test formatting on file"""
        self.highscores.highscore = {"Oliver": 20, "Marcus": 18}
        
        self.highscores.seperate_highscores(file_path=self.test_file_path)
        
        with open(self.test_file_path, 'r') as file:
            """Test file formatting on test_file.txt"""
            for line in file:
                line = line.strip()
                parts = line.split(':')
                
                self.assertEqual(len(parts), 2)
                self.assertIsInstance(parts[0].strip(), str)
                self.assertIsInstance(parts[1].strip(), str)
                self.assertTrue(parts[1].strip().isdigit())
                
if __name__=="__main__":
    unittest.main()