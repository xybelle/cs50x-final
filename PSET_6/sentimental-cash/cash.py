from cs50 import get_float


def main():
    cents = get_cents()
    quarters = calc_quarters(cents)
    cents = cents - quarters * 25

    dimes = calc_dimes(cents)
    cents = cents - dimes * 10

    nickels = calc_nickels(cents)
    cents = cents - nickels * 5

    pennies = calc_pennies(cents)
    cents = cents - pennies * 1

    coins = quarters + dimes + nickels + pennies
    print(coins)


def get_cents():
    while True:
        c = get_float("Change owed: ")
        if c > 0:
            return c
        else:
            pass


def calc_quarters(cents):
    while cents >= 25:
        cents = -25
        quarters += 1
    return quarters


def calc_dimes(cents):
    while cents >= 10:
        cents = cents - 10
        dimes += 1
    return dimes


def calc_nickels(cents):
    while cents >= 5:
        cents = cents - 5
        nickels += 1
    return nickels


def calc_pennies(cents):
    while cents >= 1:
        cents = cents - 1
        pennies += 1
    return pennies


main()
