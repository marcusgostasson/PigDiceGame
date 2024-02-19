import dice


class Player():
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.tossed_amount = 0

    def get_total_score(self):
        return self.total_score

    def set_total_score(self, value):
        self.total_score += value

    def get_tossed_amount(self):
        return self.tossed_amount

    def set_tossed_amount(self):
        self.tossed_amount += 1

    def throwdice(self, dice):
        """ Throw the dice and add to tossed amount """
        dice_random_number = dice.get_random_number()
        self.set_tossed_amount()
        return dice_random_number

# Detta är en kommentar
