import csv

with open("something.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["language"])
