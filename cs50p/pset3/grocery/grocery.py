grocery_list = {}
while True:
    try:
        item = input()
        grocery_list[item] = 1
        grocery_list.get(item)
    except EOFError:
        print(grocery_list)
        break
