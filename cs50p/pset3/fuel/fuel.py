try:
    fraction = input("Fraction: ").split()
    percent = float(fraction[0]) / float(fraction[2])
except ValueError:
    print

print(f"{float(percent)}%")
