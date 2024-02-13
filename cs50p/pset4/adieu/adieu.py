names = {}
while True:
    try:
        name = input("Name: ")
        names[name] = 1
    except EOFError:
        print("Adiue, addieu, to ", end="")
        for name in names:
            print(f"{name)

