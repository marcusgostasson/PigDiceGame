class Highscore:
    def __init__(self):
        self.highscores = {}
    
    def add_winner(self, player):
        if player in self.highscores:
            self.increase_score(player)
        else:
            score = 1
            self.highscores[player] = score
        
    def increase_score(self, player):
        self.highscores[player] += 1
    
    def sort_winners_score(self):
        sorted_highscores = sorted(self.highscores.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_highscores)
    

        
        
