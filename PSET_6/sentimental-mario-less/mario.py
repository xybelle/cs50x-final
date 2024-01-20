from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        if 0 < height <= 8:
            break
    draw(height)


def draw(h):
    for i in range(h):
        spaces = " " * (h - (i + 1))
        hashes = "#" * (i + 1)
        print(f"{spaces}{hashes}")


main()
