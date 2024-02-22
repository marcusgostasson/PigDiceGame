"""Testclass for computer"""

import unittest
from PigDiceGame import computer


class test_computer(unittest.TestCase):
    """Test the class"""

    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = computer.Computer()
        self.assertIsInstance(res, computer.Computer)


if __name__ == "__main__":
    unittest.main()
