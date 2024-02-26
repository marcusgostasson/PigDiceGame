"""Computer intelligence"""

import random
from ast import List


class Computer:
    """Class for computer"""
    def __init__(self, difficulty):
        """Constructor for computer's sum"""
        self.sum = 0
        self.difficulty = difficulty

    def difficulty_choice(choice):
        if choice == 1:
            Computer.easy_difficulty()
        elif choice == 2:
            Computer.medium_difficulty()
        elif choice == 3:
            Computer.hard_difficulty()
        elif choice == 4:
            Computer.random_difficulty()

    def hard_difficulty(self, score):
        """Method for hard_difficulty"""
        if score >= 25:
            return random.choices(List, weights=(0, 100))
        else:
            return random.choices(List, weights=(100, 0))

    def medium_difficulty(self, toss_count):
        """Method for medium_difficulty"""
        if toss_count == 0:
            return random.choices(List, weights=(100, 0))
        elif toss_count == 1:
            return random.choices(List, weights=(80, 20))
        elif toss_count == 2:
            return random.choices(List, weights=(70, 30))
        elif toss_count == 3:
            return random.choices(List, weights=(60, 40))
        elif toss_count == 4:
            return random.choices(List, weights=(50, 50))
        elif toss_count == 5:
            return random.choices(List, weights=(40, 60))
        elif toss_count == 6:
            return random.choices(List, weights=(30, 70))
        elif toss_count == 7:
            return random.choices(List, weights=(20, 80))
        elif toss_count == 8:
            return random.choices(List, weights=(0, 100))

    def easy_difficulty(self, toss_count):
        """Method for easy_difficulty"""
        if toss_count == 0:
            return random.choices(List, weights=(100, 0))
        elif toss_count == 1:
            return random.choices(List, weights=(0, 100))

    def random_difficulty(self):
        """Method for random_difficulty"""
        return random.choices(List, weights=(50, 50))
