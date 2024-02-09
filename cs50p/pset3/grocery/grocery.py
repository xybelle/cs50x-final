grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1

    except EOFError:
        print(f"{grocery_list.get(item)} {grocery_list[item]}")
        i = grocery_list.keys()
        for item in grocery_list:

            print(i[item].upper)
        break
