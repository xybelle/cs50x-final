import random

def main():
    oper = get_operation()
    n = get_level()
    match oper:
        case "+":
            score = practice_addition(n)
        case "-":
            score = practice_subtraction(n)
        case "*":
            score = practice_multiplication(n)
        case "/":
            score = practice_division(n)
    print(f"Score: {score}")


def practice_addition(n):
    correct_answer = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 1
        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if x + y == ans:
                    correct_answer += 1
                    print("Good job! 🎉")
                    break
                elif tries == 3:
                    answer = x + y
                    print(f"Answer: \n{x} + {y} = {answer}")
                    break
                else:
                    tries += 1
                    print("Try again")
            except ValueError:
                pass
    return correct_answer


def practice_subtraction(n):
    correct_answer = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 1
        for i in range(3):
            try:
                ans = int(input(f"{x} - {y} = "))
                if x + y == ans:
                    correct_answer += 1
                    break
                elif tries == 3:
                    answer = x - y
                    print(f"Answer: \n{x} - {y} = {answer}")
                    break
                else:
                    tries += 1
                    print("Try again")
            except ValueError:
                pass
    return correct_answer


def practice_multiplication():
    correct_answer = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 1
        for i in range(3):
            try:
                ans = int(input(f"{x} * {y} = "))
                if x + y == ans:
                    correct_answer += 1
                    break
                elif tries == 3:
                    answer = x + y
                    print(f"Answer: \n{x} * {y} = {answer}")
                    break
                else:
                    tries += 1
                    print("Try again")
            except ValueError:
                pass
    return correct_answer


def practice_division():
    correct_answer = 0
    for i in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        tries = 1
        for i in range(3):
            try:
                ans = int(input(f"{x} / {y} = "))
                if x + y == ans:
                    correct_answer += 1
                    break
                elif tries == 3:
                    answer = x + y
                    print(f"Answer: \n{x} / {y} = {answer}")
                    break
                else:
                    tries += 1
                    print("Try again")
            except ValueError:
                pass
    return correct_answer


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def get_level():
    while True:
        level = int(input("Level: "))
        if level <= 3 and level > 0:
            return level
        else:
            print("Select levels between 1 - 3")


def get_operation():
    operations = ("+", "-", "*", "/")
    while True:
        oper = input(
            "Addition (+) | Subtraction (-) | Multiplication (*) | Division (/)\nWhat do you want to practice today? "
            )
        if oper in operations:
            return oper
        else:
            print("Invalid operation. (use: + , - , * , /)")


if __name__ == "__main__":
    main()
