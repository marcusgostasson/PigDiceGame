"""Player class"""


class Player():
    """Constructor for Player.py"""

    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.tossed_amount = 0

    def getName(self):
        """Getter for getName method"""
        return self.name

    def get_total_score(self):
        """Getter for get_total_score"""
        return self.total_score

    def get_tossed_amount(self):
        """Getter for get_tossed_amount"""
        return self.tossed_amount

    def set_total_score(self, value):
        """Setter for set_total_score method"""
        self.total_score = value

    def set_tossed_amount(self):
        """Setter for set_tossed_amount"""
        self.tossed_amount += 1

    def throwdice(self, dice):
        """ Throw the dice and add to tossed amount """
        dice_random_number = dice.get_random_number()
        self.set_tossed_amount()
        return dice_random_number
