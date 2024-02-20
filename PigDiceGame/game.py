#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from . import player
from . import computer
from . import dice
import random
# Did we put a licence when we created the repository?


class Game:
    def __init__(self):
        pass

    def display(self):
        print("""Hello and welcome to Pig Dice Game
Press 1 if you want to play with a friend
Press 2 if you want to play vs the computer
Press 3 if you want to see the rules for the game""")

    def get_choice_from_user(self, prompting):
        try:
            choice = input(prompting)
            return int(choice)
        except ValueError:
            return None

    def startGame(self):
        while (True):
            self.display()

            choice = self.get_choice_from_user("Choice: ")

            if (choice == 1):
                player1Name = input("What is player1's name? ")
                player1 = player.Player(player1Name)
                player2Name = input("What is player2's name? ")
                player2 = player.Player(player2Name)
                playing = True
                while (playing):
                    playing = self.playerPlaying(player1)
                    if (playing is True):
                        playing = self.playerPlaying(player2)
            elif (choice == 2):
                playerName = input("What is your name? ")
                player1 = player.Player(playerName)
                difficulty = int(input("""What difficulty do you want?
1. Playing against a new born baby
2. Playing against my uncle that is pretty good with numbers
3. Playing against Pelle, if you know you know
4. Completly random no logic"""))
                computer = computer.Computer(difficulty)
                playing = True
                while (playing):
                    playing = self.playerPlaying(player1)
                    if (playing is True):
                        playing = self.computerPlaying(computer)

            elif (choice == 3):
                print("""\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n""")

            else:
                print("Invalid input")

    def playerPlaying(self, currentPlayer):
        die = dice.Dice()
        score = currentPlayer.get_total_score()  # Getting score from the player
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            print(currentPlayer.getName() + " you currently have " + str(score) + " point(s)")
            choice = input(currentPlayer.getName() + " do you want to toss or stay? ")
            choice = choice.lower().strip()

            if (choice == "toss"):
                dieValue = currentPlayer.throwdice(die)
                print(currentPlayer.getName() + " got a " + str(dieValue))
                if (dieValue != 1):
                    score += dieValue
                    gameIsBeingPlayed = self.checkIfWinner(score)
                    continue
                else:
                    print("Oh you got a " + str(dieValue) + " better luck next time\n")
                    gameIsBeingPlayed = False
                    return True

            elif (choice == "stay"):
                currentPlayer.set_total_score(score)
                currentPoints = currentPlayer.get_total_score()
                print(currentPlayer.getName() + " stayed and now have " + str(currentPoints) + " point(s)\n")
                gameIsBeingPlayed = False
                return True

            else:
                print("Invalid option!")  # Can make this print in red
        return False

    def computerPlaying(self, computer):
        die = dice.Dice()
        difficulty = computer.getDifficulty()
        score = computer.get_total_score()  # Getting score from the computer
        gameIsBeingPlayed = True
        options = ["toss", "stay"]
        tossCounter = 0 # something with the first toss is 100% toss then i change weight based on how many toss
        while (gameIsBeingPlayed):
            print(computer.getName() + " you currently have " + str(score) + " point(s)")
            pick = random.choices(options, weights=difficulty) # Problem can be with logic to stay at 20 because now the logic is weight based

            choice = pick
            if (choice == "toss"):
                dieValue = computer.throwdice(die)
                print(computer.getName() + " got a " + str(dieValue))
                if (dieValue != 1):
                    score += dieValue
                    gameIsBeingPlayed = self.checkIfWinner(score)
                    continue
                else:
                    print("Oh you got a " + str(dieValue) + " better luck next time\n")
                    gameIsBeingPlayed = False
                    return True

            elif (choice == "stay"):
                computer.set_total_score(score)
                currentPoints = computer.get_total_score()
                print(computer.getName() + " stayed and now have " + str(currentPoints) + " point(s)\n")
                gameIsBeingPlayed = False
                return True

            else:
                print("Invalid option!")  # Can make this print in red
        return False

    def checkIfWinner(self, score):
        if (score >= 100):
            print("You got over 100 and won!")  # can make this green
            return False
        else:
            return True
