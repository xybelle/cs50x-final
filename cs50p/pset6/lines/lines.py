import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.startswith("#")
                continue
            elif line.lstrip()
except FileNotFoundError:
    sys.exit("File does not exist")
