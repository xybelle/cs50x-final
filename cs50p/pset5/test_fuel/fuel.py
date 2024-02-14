def main():
    percent = get_fraction()

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{int(round(percent))}%")


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ").split('/')
            percent = (int(fraction[0]) / int(fraction[1])) * 100
            if percent > 100:
                raise ExceedHundred
            return percent
        except (ValueError, ZeroDivisionError, ExceedHundred):
            pass


class ExceedHundred(Exception):
    pass


if __name__ == "__main__"
    main()


def main():
    f = input("Fraction: ")
    convert(f)
    

def convert(fraction):
    z = fraction.split('/')
    x = int(z[0])
    y = int(z[1])
    try:
        if x > y:
            raise ValueError
        percent = ( x / y ) * 100
        return percent
    except (ValueError, ZeroDivisionError):
        pass
