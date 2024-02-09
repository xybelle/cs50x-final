grocery_list = [{}]
while True:
    try:
        item = input()
        li= 1

    except EOFError:
        for item in grocery_list:
            print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
