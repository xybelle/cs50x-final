while True:
    try:
        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
        break
    except ValueError:
        print
    else:
        print(f"{float(percent)}%")
