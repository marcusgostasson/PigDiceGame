"""Testclass for computer."""

import unittest
from PigDiceGame import computer


class TestComputer(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = computer.Computer("1")
        self.assertIsInstance(res, computer.Computer)

    def test_easy_difficulty_toss(self):
        """Test easy_difficulty_toss."""
        c = computer.Computer("1")
        res = c.easy_difficulty(0)
        exp = ['toss']
        self.assertEqual(res, exp)

    def test_easy_difficulty_stay(self):
        """Test easy_difficulty_stay."""
        c = computer.Computer("1")
        res = c.easy_difficulty(1)
        exp = ['stay']
        self.assertEqual(res, exp)

    def test_medium_difficulty_toss(self):
        """Test medium_difficulty_toss."""
        c = computer.Computer("2")
        res = c.medium_difficulty(0)
        exp = ['toss']
        self.assertEqual(res, exp)

    def test_medium_difficulty_stay(self):
        """Test medium_difficulty_stay."""
        c = computer.Computer("2")
        res = c.medium_difficulty(8)
        exp = ['stay']
        self.assertEqual(res, exp)

    def test_hard_difficulty_toss(self):
        """Test hard_difficulty_toss."""
        c = computer.Computer("Pelle")
        res = c.hard_difficulty(24)
        exp = ['toss']
        self.assertEqual(res, exp)

    def test_hard_difficulty_stay(self):
        """Test hard_difficulty_stay."""
        c = computer.Computer("Pelle")
        res = c.hard_difficulty(25)
        exp = ['stay']
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
