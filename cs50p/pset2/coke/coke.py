print("Amount due: 50")
amount_due = 50
valid_c = [25, 10, 5]
c = int(input("Insert coin: "))
while amount_due != 0:
    if c in valid_c:
        amount_due -= c
        if amount_due == 0:
            print("Change owed: 0")
        print(f"Amount due: {amount_due}")
        c = int(input("Insert coin: "))
    else:
        print(f"Amount due: {amount_due}")
