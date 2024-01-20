from cs50 import get_int

def draw(n):
    # Base case
    if n == 1:
        return 1
    # Recursive call
    else:
        print("#" * draw(n - 1))

height = get_int("Height: ")
draw(height)
