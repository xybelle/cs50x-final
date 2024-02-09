grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        for item in grocery_list:

            print(f"{grocery_list.get(item)} {grocery_list.keys()}")
        break
