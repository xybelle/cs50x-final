while True:
    try:
        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
        break
    except ValueError:
        pass

print(f"{float(percent)}%")
