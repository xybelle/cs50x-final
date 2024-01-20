from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 8 or height < 0:
            pass
        draw(height)

def draw(h):
    # If nothing to draw
    if h <= 0:
        return;

    # Print pyramid of height h - 1
    draw(h - 1)

    for i in range(i < h):
        print("#")

main()
