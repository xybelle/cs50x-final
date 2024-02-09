grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        key = grocery_list.keys()
        for item in grocery_list:

            print(f"{grocery_list.get(item)} {s.upper = item}")
        break
