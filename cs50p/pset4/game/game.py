import random


def main():
    while True:
        try:
            number = input("Level: ")
            if n <= 0:
                raise ValueError
            guess(n)
        except ValueError:
            pass


def guess(number):
    while True:
        try:
            n = random.randint(1, number)
            g = input("Guess: ")
            if g == n:
                print("Just right!")
            elif g < n:
                print("Too small!")
            elif g > n:
                print("Too large!")
            else:
                raise ValueError
        except ValueError:
            pass


main()
