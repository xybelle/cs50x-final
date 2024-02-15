import sys

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


if __name__ == "__main__":
    main()
