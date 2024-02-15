#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import Player
import Computer 


class Game:
    def __init__(self):
        pass

    def display(self):
        print("Hello and welcome to Pig Dice Game\n")
        print("Press 1 if you want to play with a friend")
        print("Press 2 if you want to play vs the computer")
        print("Press 3 if you want to see the rules for the game")

    def startGame(self):
        self.display()
        choice = int(input("Choice: "))
        if (choice == 1):
            player1 = input("What is your name? ")
            player2 = input("What is your name? ")
            playing = True
            while (playing):
                playing = self.playerAgainstPlayer(player1)
                playing = self.playerAgainstPlayer(player2)

    def playerAgainstPlayer(self, currentPlayer, dice):
        if isinstance(currentPlayer, Player()):
            score = currentPlayer.getAmount()  # Getting score from the player
            gameIsBeingPlayed = True
            while (gameIsBeingPlayed):
                choice = input(currentPlayer.getName() + " do you want to toss or stay? ")
                choice = choice.lower().strip()

                if (choice == "toss"):
                    dieValue = currentPlayer.tossDice(dice)
                    if (dieValue != 1):
                        score += dieValue
                        gameIsBeingPlayed = self.checkIfWinner(currentPlayer)
                        continue
                    else:
                        gameIsBeingPlayed = False

                elif (choice == "stay"):
                    gameIsBeingPlayed = False
                    currentPlayer.setTotalPoints(score)

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

    def checkIfWinner(self, player):
        playerPoints = player.getPoints()
        if (playerPoints > 100):
            print("You won!")  # can make this green
            return False
