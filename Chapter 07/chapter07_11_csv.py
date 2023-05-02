import csv
from pathlib import Path

filepath = "./testing_files/countries.csv"
with Path(filepath).open() as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        print(row)