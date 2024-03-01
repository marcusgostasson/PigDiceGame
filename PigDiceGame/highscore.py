"""Highscore class."""


class Highscore:
    """Class to initiate highscore."""

    def __init__(self):
        """Initialize highsscore list."""
        self.highscores = {}

    def add_winner(self, player):
        """Add winner a winner."""
        if player in self.highscores:
            self.highscores[player] += 1
        else:
            score = 1
            self.highscores[player] = score

    def get_name_and_highscore(self):
        """Class method to get name and score."""
        names = []
        values = []

        playerlist = self.sorted_list()
        for keys_values in playerlist:
            name, value = keys_values
            names.append(name)
            values.append(value)
        return names, values

    def add_highscore_to_file(self, highscores):
        """Class method to add highscores to file."""
        with open("highscore_list.txt", 'w', encoding='utf-8') as file:
            for name, score in highscores.items():
                file.write(f"{name} : {score}\n")

    def retreive_highscore_file(self):
        """Class method to retreive highscore file."""
        highscores = {}
        with open("highscore_list.txt", 'r', encoding='utf-8') as file:
            for line in file:
                name, score = line.srip().split(':')
                highscores[name] = int(score)
        return highscores

    def sorted_list(self):
        """Class method to sort highscores."""
        sorted_highscores = sorted(self.highscores.items(), key=lambda x: x[1],
                                   reverse=True)
        return sorted_highscores
