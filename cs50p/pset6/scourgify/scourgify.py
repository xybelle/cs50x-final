import csv
import sys


from tabulate import tabulate


def main():
    # Ensure user prove two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    data = read_csv()
    processed_data = process_csv(data)
    write_csv(processed_data)


def read_csv():
    raw_data = []
    # Error handling when reading CSV and appending raw_data dict
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                raw_data.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    return raw_data


def process_csv(data):
    processed_data = []
    # Splitting name into first name and last name
    # Append first, last, house into processed_data dict
    for row in data:
        sname, fname = row["name"].lstrip().split(",")
        house = row["house"]
        processed_data.append({"first name": fname, "last name": sname, "house": house})
    return processed_data


def write_csv(processed_data):
    # Writing new CSV
    with open(sys.argv[2], "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first name", "last name", "house"])
        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)


if __name__ == "__main__":
    main()
