import os
import sys

from PIL import Image


valid_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]

def main():
    if not valid():
        sys.exit()
    #get_images()


def get_images():
    images = []
    for arg in sys.argv:
       image = Image.open(arg)


def valid():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments\nUsage: python shirt.py input output")
        return False
    elif len(sys.argv) > 3:
        print("Too many command-line arguments\nUsage: python shirt.py input output")
        return False
    temp_a = os.path.splitext(sys.argv[1])
    temp_b = os.path.splitext(sys.argv[2])
    if temp_a[1] != temp_b[1]:
        print("Input and output have different extensions")
        return False
    if temp_a[1] not in valid_extensions and temp_b[1] not in valid_extensions:
        print("Invalid input or output extension(s)")
        return False
    return True


if __name__ == "__main__":
    main()
