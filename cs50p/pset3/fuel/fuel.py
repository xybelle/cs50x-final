while True:
    try:
        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
    except ValueError:
        print("That was not a fraction")
    else:
        break

print(f"{float(percent)}%")
