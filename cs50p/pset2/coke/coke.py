print("Amount due: 50")
amount_due = 50
c = int(input("Insert coin: "))

while amount_due != 0:
    amount_due -= c
    print(f"Amount due: {amount_due}")
    c = int(input("Insert coin: "))
