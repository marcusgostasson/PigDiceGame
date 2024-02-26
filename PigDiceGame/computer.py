"""Computer intelligence"""
import random
import dice


class Computer:
    """Class for computer"""
    def __init__(self, difficulty):
        """Constructor for computer's sum"""
        self.sum = 0
        self.difficulty = difficulty
        self.options = ["toss" , "stay"]

    def difficulty_choice(self, toss_counter, score):
        if self.difficulty == 1:
            self.easy_difficulty(toss_counter)
        elif self.difficulty == 2:
            self.medium_difficulty(toss_counter)
        elif self.difficulty == 3:
            self.hard_difficulty(toss_counter, score)
        elif self.difficulty == 4:
            self.random_difficulty()

    def set_total_score(self, score):
        self.sum = score

    def get_total_score(self):
        return self.sum
    
    def throw_dice(self, die):
        return die.get_random_number()
    
    def hard_difficulty(self, score):
        """Method for hard_difficulty"""
        if score >= 25:
            return random.choices(self.options, weights=(0, 100))
        else:
            return random.choices(self.options, weights=(100, 0))

    def medium_difficulty(self, toss_count):
        """Method for medium_difficulty"""
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
        """Method for easy_difficulty"""
        if toss_count == 0:
            return random.choices(self.options, weights=(100, 0))
        elif toss_count == 1:
            return random.choices(self.options, weights=(0, 100))

    def random_difficulty(self):
        """Method for random_difficulty"""
        return random.choices(self.options, weights=(50, 50))
