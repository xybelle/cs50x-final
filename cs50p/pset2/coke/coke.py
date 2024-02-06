amount_due = 50, c = 0, change = 0
valid_c = [25, 10, 5]

while amount_due != 0:
    print(f"Amount due: {amount_due}")
    c = int(input("Insert coin: "))
    if c in valid_c:
        amount_due -= c
        if amount_due == 0:
            print("Change owed: 0")
        print(f"Amount due: {amount_due}")
        c = int(input("Insert coin: "))
    else:
        print(f"Amount due: {amount_due}")
        break
    continue
