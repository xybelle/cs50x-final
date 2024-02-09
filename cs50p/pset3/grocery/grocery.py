grocery_list = {'item'}
while True:
    try:
        item = input()
        grocery_list['item'] = item

    except EOFError:
        print(grocery_list)
        break
