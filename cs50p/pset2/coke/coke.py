amount_due, c = 50, 0
valid_c = [25, 10, 5]

while c <= 50:
    print(f"Amount due: {amount_due}")
    c = int(input("Insert coin: "))
    if c not in valid_c:
        continue
    else:
        amount_due -= c
        if amount_due <= 0:
            break

change = amount_due - c
print(f"Change owed: {change}")
