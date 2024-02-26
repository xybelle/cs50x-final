import random

def main():
    oper = get_operation()
    level = get_level()
    score = practice_arithmetic(level, oper)
    print(f"Your score is: {score} 👌\nExiting...")


def practice_arithmetic(n, operation):
    correct_answer = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 1
        for i in range(3):
            try:
                ans = int(input(f"{x} {operation} {y} = "))
                if eval(f"{x} {operation} {y}") == ans:
                    correct_answer += 1
                    print("🤩")
                    break
                elif tries == 3:
                    answer = eval(f"{x} {operation} {y}")
                    print(f"Answer: \n{x} {operation} {y} = {answer} 👈")
                    break
                else:
                    tries += 1
                    print("Try again 🙁")
            except ValueError:
                pass
    return correct_answer


def generate_integer(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 3 and level > 0:
                return level
            else:
                raise ValueError
        except ValueError:
            print("\n\033[3mSelect levels between 1 - 3\033[0m\n")
            pass


def get_operation():
    operations = ("+", "-", "*", "/")
    while True:
        oper = input(
            "Addition (+) | Subtraction (-) | Multiplication (*) | Division (/)\nWhat do you want to practice today? "
            )
        if oper in operations:
            return oper
        else:
            print("\n\033[3mInvalid operation. (use: + , - , * , /)\033[0m\n")


if __name__ == "__main__":
    main()
