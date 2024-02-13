import random


def main():
    n = get_level()
    correct_ans = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 0
        for i in range(3)
            try:
                ans = int(input(f"{x} + {y} = "))
                if x + y == ans:
                    correct_ans += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                    raise ValueError

                if tries == 3:
                    print(f"{x} + {y} = {answer}", answer = x + y)
                    continue
            except ValueError:
                pass


def get_level():

        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
