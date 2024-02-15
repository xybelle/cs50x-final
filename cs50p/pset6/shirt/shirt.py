import sys


valid_extensions = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]


def main():
    if not valid():
        sys.exit(f"{message}")


def valid():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        message = "Too few command-line arguments\nUsage: python shirt.py input output"
    elif len(sys.argv) > 3:
        message = "Too many command-line arguments\nUsage: python shirt.py input output"

    temp1 = sys.argv[1].split(".")
    temp2 = sys.argv[2].split(".")

    if temp1[1] != temp2[1]:
        message = "Input and output have different extensions"
    if temp1[1] not in valid_extensions and temp2[1] not in valid_extensions:
        message = "Invalid input or output extension(s)"

    return message


if __name__ == "__main__":
    main()
