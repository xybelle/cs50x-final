while True:

        fraction = input("Fraction: ").split()
        percent = float(fraction[0]) / float(fraction[2])
        break


print(f"{float(percent)}%")
