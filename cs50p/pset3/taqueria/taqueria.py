menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    while true:
        try:
            


w
total = 0
while True:
    try:
        item = input("Item: ").title()
        if item not in menu:
            raise NotInMenu
        total += menu[f'{item}']
        print(f"${float(total)}")
    except EOFError:
        break
    else:
        pass

