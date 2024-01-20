from cs50 import get_int

def main():
    while True:
        height = get_int("Height: ")
        if height > 8 or height < 0:
            pass
        else:
            draw(height)

def draw(h):
    if h == 1:
        return 1
    else:
        for i in range(h):
            print("#" * h * draw(h-1))

main()
