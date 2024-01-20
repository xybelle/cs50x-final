from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 0 or height < 8:
            break
    draw(height)


def draw(h):
    for i in range(h + 1):
        print(" " * h, end="")
        print("#" * i)
    print()


main()
