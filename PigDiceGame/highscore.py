class Highscore:
    def __init__(self):
        self.highscores = {}
    
    def add_winner(self, player):
        if player in self.highscores:
            self.increase_score(player)
        else:
            score = 1
            self.highscores[player] = score
        
    def get_name_and_highscore(self):
        names = []
        values = []

        playerlist = self.sorted_list()
        for keys_values in playerlist:
            name, value = keys_values
            names.append(name)
            values.append(value)
        return names, values

    def sorted_list(self):
        sorted_highscores = sorted(self.highscores.items(), key=lambda x: x[1], reverse=True)
        return sorted_highscores

