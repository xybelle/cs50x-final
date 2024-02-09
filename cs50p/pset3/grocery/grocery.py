grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        print(f"{grocery_list.get(item)} {grocery_list[item]}")
        print(iter(grocery_list.keys()))
        break
