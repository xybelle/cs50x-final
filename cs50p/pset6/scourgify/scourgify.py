import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
#elif ".csv" not in sys.argv[1] and ".csv" not in sys.arg[2]:
#    sys.exit("Not a CSV file")

before = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            before.append(row)
        print(before)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

