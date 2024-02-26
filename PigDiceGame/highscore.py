class Highscore:
    def __init__(self):
        self.highscores = {}
        
        try:
            open('highscore_list.txt', 'x').close()
        except FileExistsError:
            pass
        
    def apply_score(self, player_name, score):
        self.highscores[player_name] = score
        
    def get_highscore(self):
        return self.highscores
        
    def seperate_highscores(self):
        exsisting_highscores = {}
        try:
            with open ('highscore_list.txt', 'r') as file:
                for line in file:
                    if line.strip():
                        name, score = line.split(':')
                        exsisting_highscores.setdefault(name.strip(), []).append(int(score.strip()))
        except FileNotFoundError:
            print("File error")
        
        for name, score in self.highscores.items():
            score = int(score.strip())
            exsisting_highscores.setdefault(name, [].append(score))
        
        sorted_highscores = sorted(exsisting_highscores.items(), key=lambda x: max(x[1]), reverse=True)
        
        with open ('highscore_list.txt', 'a') as file:
            for name, scores in sorted_highscores:
                for score in scores:
                    file.write(f"{name} : {score}\n")
                    
        
        
