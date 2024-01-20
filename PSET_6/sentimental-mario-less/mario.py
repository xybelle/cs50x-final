from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 0 or height < 8:
            break
    draw(height)


def draw(h):
    for i in range(h):
        for j in range(h):
            print("*", end="")
        for k in range(i):
            print("#", end="")
        print()


main()
