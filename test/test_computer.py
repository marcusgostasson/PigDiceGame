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

    def test_medium_difficulty(self):
        """Test for medium_difficulty."""
        c = computer.Computer("2")
        res = c.medium_difficulty(1)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(2)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(3)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(4)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(5)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(6)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

        c = computer.Computer("2")
        res = c.medium_difficulty(7)
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

    def test_random_difficulty(self):
        """Test for random difficulty"""
        c = computer.Computer
        res = c.random_difficulty
        exp = (['stay'], ['toss'])
        self.assertIn(res, exp)

    def test_difficulty_choice(self):
        """Test for choosing difficulty"""
        c = computer.Computer
        res = c.difficulty_choice
        self.assertIsNotNone(res)


if __name__ == "__main__":
    unittest.main()
