import random


def main():
    sum = 0
    random_number = random.int(1, 6)
    if random_number != 1:
        while True:
            sum += random_number
            print("Sum of computers numbers: {sum}")
            if sum >= 20:
                print("Computer decided to hold at {sum}")
                break
            else:
                break