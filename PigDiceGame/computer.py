"""Computer intelligence."""
import random


class Computer:
    """Class for computer."""

    def __init__(self, difficulty):
        """Instanciate for computer's sum."""
        self.tossed_amount = 0
        self.sum = 0
        self.difficulty = difficulty
        self.options = ["toss", "stay"]

    def difficulty_choice(self, toss_counter, score):
        """Class method for choosing difficulty."""
        if self.difficulty == "1":
            option = self.easy_difficulty(toss_counter)
            return option
        elif self.difficulty == "2":
            option = self.medium_difficulty(toss_counter)
            return option
        elif self.difficulty == "Pelle":
            option = self.hard_difficulty(score)
            return option
        elif self.difficulty == "4":
            option = self.random_difficulty()
            return option

    def set_total_score(self, score):
        """Setter for sum of computer."""
        self.sum = score

    def get_total_score(self):
        """Getter for sum of computer."""
        return self.sum

    def set_tossed_amount(self):
        """Setter for amount of tosses the computer has done."""
        self.tossed_amount += 1

    def get_tossed_amount(self):
        """Getter for amount of tosses the computer has done."""
        return self.tossed_amount

    def throw_dice(self, die):
        """Class method for throwing the dice."""
        self.set_tossed_amount()
        return die.get_random_number()

    def hard_difficulty(self, score):
        """Class method for hard_difficulty."""
        if score >= 25:
            return random.choices(self.options, weights=(0, 100))
        else:
            return random.choices(self.options, weights=(100, 0))

    def medium_difficulty(self, toss_count):
        """Class method for medium_difficulty."""
        if toss_count == 0:
            return random.choices(self.options, weights=(100, 0))
        elif toss_count == 1:
            return random.choices(self.options, weights=(80, 20))
        elif toss_count == 2:
            return random.choices(self.options, weights=(70, 30))
        elif toss_count == 3:
            return random.choices(self.options, weights=(60, 40))
        elif toss_count == 4:
            return random.choices(self.options, weights=(50, 50))
        elif toss_count == 5:
            return random.choices(self.options, weights=(40, 60))
        elif toss_count == 6:
            return random.choices(self.options, weights=(30, 70))
        elif toss_count == 7:
            return random.choices(self.options, weights=(20, 80))
        elif toss_count == 8:
            return random.choices(self.options, weights=(0, 100))

    def easy_difficulty(self, toss_count):
        """Class method for easy_difficulty."""
        if toss_count == 0:
            return random.choices(self.options, weights=(100, 0))
        elif toss_count == 1:
            return random.choices(self.options, weights=(0, 100))

    def random_difficulty(self):
        """Class method for random_difficulty."""
        return random.choices(self.options, weights=(50, 50))
