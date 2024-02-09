grocery_list = [{}]
while True:
    try:
        item = input()
        grocery_list = item


    except EOFError:
        #or item in grocery_list:
            #print(f"{grocery_list.get(item)} {item.upper()}")
        print(grocery_list)
        break
