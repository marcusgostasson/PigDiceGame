"""Computer class"""

import random


class Computer:
    """Class to represent computer"""

    def init(self):
        """Constructor for Computer"""
        self.sum = 0

    def hard_difficulty(self):
        """Method for hard_difficulty"""
        sum = 0
        while True:
            random_number = random.randint(1, 6)
            if random_number != 1:
                self.sum += random_number
                sum += random_number
                print(f"The computer rolled a {random_number}")
                print(f"Sum of computers numbers: {self.sum}")
                if sum >= 25:
                    print(f"The computer decided to hold at: {self.sum}")
                break
            elif random_number == 1:
                print("The computer threw a 1. Sum for the computer is now 0")
                self.sum = 0
                break

    def medium_difficulty(self):
        """Method for medium_difficulty"""
        sum = 0
        for i in range(1, 10):
            throw_percentage = random.randint(1, i)
            if throw_percentage == 1:
                random_number = random.randint(1, 6)
                if random_number != 1:
                    self.sum += random_number
                    sum += random_number
                    print(f"The computer rolled a {random_number}")
                    print(f"Sum of computers number: {self.sum}")
                elif random_number == 1:
                    print("The computer threw a 1. Sum for the computer is now 0")
                    self.sum = 0
                    break
            else:
                print(f"The computer decided to hold at: {self.sum}")
                break

    def easy_difficulty(self):
        """Method for easy_difficulty"""
        randomnumber = random.randint(1, 6)
        if randomnumber != 1:
            self.sum += randomnumber
            print(f"The computer rolled a {random_number}")
            print(f"Sum of computers number: {self.sum}")
        elif random_number == 1:
            print("The computer threw a 1. Sum for the computer is now 0")
            self.sum = 0
        print(f"The computer decided to hold at: {self.sum}")

    def random_difficulty(self):
        """Method for random_difficulty"""
        while True:
            random_number = random.randint(1, 6)
            if random_number != 1:
                self.sum += random_number
                print(f"The computer rolled a {random_number}")
                print(f"Sum of computers number: {self.sum}")
            elif random_number == 1:
                print("The computer threw a 1. Sum for the computer is now 0")
                self.sum = 0
                break
            throw_percentage = random.randint(1, 2)
            if throw_percentage == 1:
                print(f"The computer decided to hold at: {self.sum}")
                break

    if __name__ == "__main__":

        computer = Computer()
        hard_difficulty(computer)
        medium_difficulty(computer)
        easy_difficulty(computer)
        random_difficulty(computer)
