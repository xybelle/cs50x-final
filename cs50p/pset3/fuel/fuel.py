while True:
    try:
        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
    except ValueError:
        print("x is not a fraction")
    else:
        break

print(f"{float(percent)}%")
