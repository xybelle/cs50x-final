grocery_list = {}
while True:
    try:
        item = input()
        grocery_list = item

    except EOFError:
        print(grocery_list)
        break
