"""Player Class."""


class Player:
    """Class to represent a player."""

    def __init__(self, name):
        """Initialize player attributes."""
        self.name = name
        self.total_score = 0
        self.tossed_amount = 0

    def get_name(self):
        """Getter for player's name."""
        return self.name

    def get_total_score(self):
        """Getter for player's total score."""
        return self.total_score

    def get_tossed_amount(self):
        """Getter for the number of times the player tossed the dice."""
        return self.tossed_amount

    def set_name(self, name):
        """Setter to set a new name for the player."""
        self.name = name

    def set_total_score(self, value):
        """Setter for player's total score."""
        self.total_score = value

    def set_tossed_amount(self):
        """Increment the number of times the player tossed the dice."""
        self.tossed_amount += 1

    def throw_dice(self, dice):
        """Throw the dice and increment tossed amount."""
        try:
            dice_random_number = dice.get_random_number()
            self.set_tossed_amount()
            return dice_random_number
        except Exception as e:
            print(f"Error while throwing dice: {e}")
            return None
