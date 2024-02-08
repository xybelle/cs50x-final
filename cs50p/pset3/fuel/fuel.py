while True:
    try:
        fraction = input("Fraction: ").split('/')
        percent = (int(fraction[0]) / int(fraction[1])) * 100

        if percent <= 0.01:
            print("E")
        elif percent >= 99:
            print("F")
        elif percent <= 100:
            print(f"{int(percent)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass


