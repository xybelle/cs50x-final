def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.lstrip('$'))
    print(d)
    return d


def percent_to_float(p):
    p = float(p.removesuffix('%'))
    print(p)
    return p


main()
