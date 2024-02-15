import sys


valid_extensions = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]


def main():
    if not valid():
        sys.exit()


def valid():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments\nUsage: python shirt.py input output")
        return False
    elif len(sys.argv) > 3:
        print("Too many command-line arguments\nUsage: python shirt.py input output")
        return False
    temp1 = sys.argv[1].split(".")
    temp2 = sys.argv[2].split(".")
    if temp1[1] != temp2[1]:
        print("Input and output have different extensions")
        return False
    if temp1[1] not in valid_extensions and temp2[1] not in valid_extensions:
        print("Invalid input or output extension(s)")
        return False
    return True


if __name__ == "__main__":
    main()
