import sys

valid_extensions = ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG"]
def main():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments\nUsage: python shirt.py input output")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments\nUsage: python shirt.py input output")

    temp1 = sys.argv[1].split(".")
    temp2 = sys.argv[2].split(".")

    if temp1[1] != temp2[1]:
        sys.exit("Input and output have different extensions")
    if temp1[1] not in valid_extensions and temp2[1] not in valid_extensions:
        sys.exit("Invalid input or output extension(s)")

    


if __name__ == "__main__":
    main()
