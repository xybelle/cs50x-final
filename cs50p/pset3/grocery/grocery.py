grocery_list = {}
while True:
    try:
        item = input()
        #ls = {'name': item, 'amt': 1}
        if item in grocery_list:
            grocery_list[item] += 1
        grocery_list[item] = 1
    except EOFError:
        for item in grocery_list:
            print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
