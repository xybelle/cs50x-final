amount_due, c, change = 50, 0, 0
valid_c = [25, 10, 5]

while c <= 50:
    print(f"Amount due: {amount_due}")
    c = int(input("Insert coin: "))
    c += c
    if c in valid_c:
        amount_due -= c
        if c <= 4:
            print(f"Change owed: {change}", change = c - amount_due)
    continue
