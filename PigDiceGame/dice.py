"""Dice class."""
import random


class Dice:
    """Class to represent a Dice."""

    def __init__(self):
        """Initialize Dice attributes."""
        self.die = 1

    def get_random_number(self):
        """Class method for getting a random number."""
        die = random.randint(1, 6)
        return die
