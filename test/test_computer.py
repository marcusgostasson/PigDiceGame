"""Testclass for computer"""

import unittest
from PigDiceGame import computer


class test_computer(unittest.TestCase):
    """Test the class"""

    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = computer.Computer()
        self.assertIsInstance(res, computer.Computer)

    def test_easy_difficulty_toss(self):
        c = computer.Computer()
        res = c.easy_difficulty(0)
        exp = "toss"
        self.assertEqual(res, exp)

    def test_easy_difficulty_stay(self):
        c = computer.Computer()
        res = c.easy_difficulty(1)
        exp = "stay"
        self.assertEqual(res, exp)

    def test_medium_difficulty_toss(self):
        c = computer.Computer()
        res = c.medium_difficulty(0)
        exp = "toss"
        self.assertEqual(res, exp)

    def test_medium_difficulty_stay(self):
        c = computer.Computer()
        res = c.medium_difficulty(8)
        exp = "stay"
        self.assertEqual(res, exp)

    def test_hard_difficulty_toss(self):
        c = computer.Computer()
        res = c.hard_difficulty(24)
        exp = "toss"
        self.assertEqual(res, exp)

    def test_hard_difficulty_stay(self):
        c = computer.Computer()
        res = c.hard_difficulty(25)
        exp = "stay"
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
