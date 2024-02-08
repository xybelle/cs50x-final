while True:

        fraction = input("Fraction: ").split('/')
        percent = (int(fraction[0]) / int(fraction[1])) * 100
        break


print(f"{percent}%")
