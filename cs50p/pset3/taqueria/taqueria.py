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
    item = get_item()
    total =


def get_item():
    while True
        try:
            item = input("Item: ")
            if item not in menu:
                raise NotInMenu
            return item
        except (NotInMenu, EOFError):
            pass

class NotInMenu(Exception):
    pass
