grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        print(grocery_list.items())
        break
