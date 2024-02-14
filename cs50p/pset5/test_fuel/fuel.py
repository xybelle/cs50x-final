def main():
    f = input("Fraction: ")
    convert(f)
    print(gauge)


def convert(fraction):
    z = fraction.split('/')
    x = int(z[0])
    y = int(z[1])
    try:
        if x > y:
            raise ValueError
        percent = ( x / y ) * 100
        return gauge(int(round(percent)))
    except (ValueError, ZeroDivisionError):
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
