while True:
    try:
        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
        break
    except ValueError:
        print("That was not a fraction")

print(f"{float(percent)}%")
