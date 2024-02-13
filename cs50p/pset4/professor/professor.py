import random


def main():
    get_level()

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
            generate_integer(level)
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        random_number = random.randint(1, 9)
    elif level == 2:
        random_number = random.randint(10, 99)
    elif level == 3:
        random_number = random.randint(100, 999)


if __name__ == "__main__":
    main()
