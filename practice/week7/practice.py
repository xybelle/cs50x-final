import csv

with open("something.csv", "r") as file:
    reader = csv.DictReader(file)
    scratch, c, python = 0, 0, 0

    for row in reader:
        favorite = 
