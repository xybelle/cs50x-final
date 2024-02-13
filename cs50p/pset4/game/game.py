import random

while True:
    try:
        n = input("Level: ")
        if n <= 0:
            raise ValueError
        guess(n)
    except ValueError:
        pass


def guess(n):
    
