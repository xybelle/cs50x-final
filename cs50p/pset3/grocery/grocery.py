grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        key = grocery_list.keys()
        for item in grocery_list:
            s = item
            print(f"{grocery_list.get(item)} {s.upper}")
        break
