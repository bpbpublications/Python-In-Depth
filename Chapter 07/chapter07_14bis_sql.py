
import sqlite3
from faker import Faker

conn = sqlite3.connect("./testing_files/people.db")
cursor = conn.cursor()

print("Creating the table.")
try:
    cursor.execute("CREATE TABLE person (firstname TEXT, lastname TEXT, address TEXT)")
except sqlite3.OperationalError:
    print("Table already exist. Nothing to do here.")

fake = Faker()

print("Populating the table with some data.")

for _ in range(0, 20):
    first = fake.first_name()
    last = fake.last_name()
    addr = fake.address()
    SQL_COMMAND = f"INSERT INTO person VALUES ('{first}', '{last}', '{addr}')"
    cursor.execute(SQL_COMMAND)

conn.commit()
conn.close()