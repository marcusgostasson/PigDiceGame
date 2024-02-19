import random


class Dice:
    def __init__(self):
        self.die = 1

    def get_random_number(self):
        die = random.randint(1, 6)
        return die
