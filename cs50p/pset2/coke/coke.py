print("Amount due: 50")
amount_due = 50
c = int(input("Insert coin: "))

for c in amount_due:
    amount_due -= c
    print(f"Amount due: {amount_due}")
    
