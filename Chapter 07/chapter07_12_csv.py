import csv
from pathlib import Path

filepath = "./testing_files/countries.csv"
with Path(filepath).open() as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        print()
        for key in row:
            if key == "Code":
                print(f"{key}: {row[key].upper()}")
            else:
                print(f"{key}: {row[key]}")
