grocery_list = [{}]
i = 0
while True:
    try:
        item = input()
        ls = {'name': item, 'amt': 1}
        grocery_list[i] = ls
        i += 1
    except EOFError:
        #for item in grocery_list:
        #    print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
