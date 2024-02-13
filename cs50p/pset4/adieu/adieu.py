import inflect


p = inflect.engine()


names =()

while True:
    try:
        name = input("Name: ")
        names = name
    except EOFError:
        #print("Adiue, addieu, to ", end="")

        print(names)
        #print(a)

