#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import Player
import Computer
import Dice


class Game:
    def __init__(self):
        pass

    def display(self):
        print("Hello and welcome to Pig Dice Game\n")
        print("Press 1 if you want to play with a friend")
        print("Press 2 if you want to play vs the computer")
        print("Press 3 if you want to see the rules for the game")

    def startGame(self):
        while (True):
            self.display()

            try:
                choice = int(input("Choice: "))
            except ValueError:
                print("Invalid input")
                continue

            if (choice == 1):
                player1Name = input("What is player1's name? ")
                player1 = Player.player(player1Name)
                player2Name = input("What is player2's name? ")
                player2 = Player.player(player2Name)
                playing = True
                while (playing):
                    playing = self.playerAgainstPlayer(player1)
                    if (playing is True):
                        playing = self.playerAgainstPlayer(player2)

            elif (choice == 3):
                print("""\nEach turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins\n""")

            else:
                print("Invalid input")

    def playerAgainstPlayer(self, currentPlayer):
        dice = Dice.Dice()
        score = currentPlayer.get_total_score()  # Getting score from the player
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            print(currentPlayer.getName() + " you currently have " + str(score) + " point(s)")
            choice = input(currentPlayer.getName() + " do you want to toss or stay? ")
            choice = choice.lower().strip()

            if (choice == "toss"):
                dieValue = currentPlayer.throwdice(dice)
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

    def playerAgainstComputer(self, computer, dice):
        computer = Computer()
        options = {1: "toss", 2: "stay"}
        tossAmount = computer.diffuculty()
        while (0 < tossAmount):
            print("Computers turn, stay or toss? ")
            choice = options.get(tossAmount)

    def checkIfWinner(self, score):
        if (score >= 100):
            print("You got over 100 and won!")  # can make this green
            return False
        else:
            return True
