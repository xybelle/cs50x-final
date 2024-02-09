grocery_list = [{}]
while True:
    try:
        item = input()
        ls = dict('name': item, 'amt': 1)

    except EOFError:
        for item in grocery_list:
            print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
