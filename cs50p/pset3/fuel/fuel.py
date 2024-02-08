def main():
    fraction = get_fraction()

    if percent <= 0.01:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{int(percent)}%")


def get_fraction(fraction):
    while True:
        try:
            fraction = input("Fraction: ").split('/')
            percent = (int(fraction[0]) / int(fraction[1])) * 100
            if percent > 100:
                percent = 'cat'
            break
        except (ValueError, ZeroDivisionError):
            pass


main()
