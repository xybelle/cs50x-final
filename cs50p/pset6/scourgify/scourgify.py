import csv
import sys

from tabulate import tabulate


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
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

after = []

for row in before:
    fname, sname  = row["name"].rstrip().split(",")
    house = row["house"]
    after.append({"first name": fname, "last name": sname, "house": house})

print(tabulate(after, headers="keys", tablefmt="grid"))

try:
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow("first" : fname)
