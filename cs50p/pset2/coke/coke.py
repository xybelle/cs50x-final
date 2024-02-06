print("Amount due: 50")
amount_due = 50
c = int(input("Insert coin: "))
valid_c = [25, 10, 5]

while amount_due != 0:
    if c in valid_c:
        amount_due -= c
        print(f"Amount due: {amount_due}")
        c = int(input("Insert coin: "))
    else:
        print(f("Amount due: {amount_due}"))
