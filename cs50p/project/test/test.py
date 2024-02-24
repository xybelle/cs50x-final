import random
import time

class Room:
    def __init__(self, description, items=None):
        self.description = description
        self.items = items if items else []

class Player:
    def __init__(self):
        self.inventory = []
        self.time_limit = 900  # 15 minutes in seconds

def display_room(room):
    print(room.description)
    if room.items:
        print("You see the following items in the room:")
        for item in room.items:
            print("- " + item)

def explore_room(room):
    display_room(room)
    action = input("What would you like to do? (Type 'help' for available actions): ").lower()
    if action == "help":
        print("Available actions: look around, take [item], go [direction]")
    elif action == "look around":
        display_room(room)
    elif action.startswith("take "):
        item_name = action.split(" ", 1)[1]
        if item_name in room.items:
            player.inventory.append(item_name)
            print(f"You take the {item_name}.")
            room.items.remove(item_name)
        else:
            print(f"There's no {item_name} in this room.")
    elif action.startswith("go "):
        print("You leave the room.")
        return True
    return False

def play_game():
    # Define rooms
    rooms = {
        "entrance": Room("You stand at the entrance of the cave. The darkness is oppressive, and the air is damp."),
        "treasure_room": Room("You enter a vast chamber filled with glittering treasures. In the center, you spot the Lost Amulet!", ["Lost Amulet"]),
        "exit": Room("You see daylight streaming in from the exit of the cave. You're almost there!")
    }

    # Connect rooms
    rooms["entrance"].exits = {"north": rooms["treasure_room"]}
    rooms["treasure_room"].exits = {"south": rooms["entrance"], "north": rooms["exit"]}
    rooms["exit"].exits = {"south": rooms["treasure_room"]}

    # Initialize player
    player = Player()
    current_room = rooms["entrance"]

    # Game loop
    print("Welcome to 'The Lost Amulet'!")
    start_time = time.time()
    while True:
        if time.time() - start_time >= player.time_limit:
            print("Time's up! You failed to escape the cave in time.")
            break

        if current_room == rooms["exit"]:
            print("Congratulations! You've found the Lost Amulet and escaped the cave!")
            break

        if explore_room(current_room):
            direction = input("Which direction would you like to go? (north/south/east/west): ").lower()
            if direction in current_room.exits:
                current_room = current_room.exits[direction]
            else:
                print("You can't go that way.")
            print()
        else:
            print()

if __name__ == "__main__":
    play_game()
