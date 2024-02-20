class Highscore:
    def __init__(self):
        self.highscores = {}
        
        try:
            open('highscore_list.txt', 'x').close()
        except FileExistsError:
            pass
          
    def round_over(self, player_name, counter):
         
     if not isinstance(player_name, str):
            raise ValueError("Player name must be a string(abc)")

        if counter <0:
            raise ValueError("Error counting score")
    
        self.highscores[player_name] = counter
        
    def apply_score(self, player_name, score):
      
        self.highscores[player_name] = score
        
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
                    
                    

highscore = Highscore()

highscore.round_over()

highscore.seperate_highscores()
        
        
