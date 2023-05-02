
import csv
from pathlib import Path

from faker import Faker
fake = Faker()


data = []
for _ in range(0, 20):
    p = {'firstname': fake.last_name(),
         'lastname': fake.last_name()}
    data.append(p)


filepath = "./testing_files/people.csv"
with Path(filepath).open(mode="a") as csv_file:
    fieldnames = ['firstname', 'lastname']
    writer = csv.DictWriter(csv_file,
                            fieldnames=fieldnames,
                            delimiter=';')

    for item in data:
        writer.writerow(item)