import random


def main():
    n = get_level()
    correct_ans = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        try:
            ans = int(input(f"{x} + {y} = "))
            if x + y == ans:
                correct_ans += 1
                continue
            else:
                raise ValueError
        except ValueError:
            pass


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
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
