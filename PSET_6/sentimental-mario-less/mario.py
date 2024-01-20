from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 8 or height < 0:
            pass
        else:
            draw(height)

def draw(h):
    # If nothing to draw
    if h <= 0:
        return;

    # Print pyramid of height h - 1
    draw(h - 1)

    # Print one more row
    for _ in range(h):
        print("#", end="")
    print()

main()
