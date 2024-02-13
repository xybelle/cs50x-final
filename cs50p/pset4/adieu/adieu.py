import inflect


p = inflect.engine()


names = p.join({})
while True:
    try:
        name = input("Name: ")
        names[name] = 1
    except EOFError:
        print("Adiue, addieu, to ", end="")
        print(names)

