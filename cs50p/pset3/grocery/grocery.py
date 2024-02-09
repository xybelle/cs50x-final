grocery_list = [{}]
while True:
    try:
        i = 0
        item = input()
        ls = {'name': item, 'amt': 1}
        grocery_list[i] = ls
        i += 1
    except EOFError:
        #for item in grocery_list:
        #    print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
