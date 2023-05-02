
import sqlite3
from faker import Faker

conn = sqlite3.connect("./testing_files/people.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE person (firstname TEXT, lastname TEXT, address TEXT)")

fake = Faker()

for _ in range(0, 20):
    first = fake.first_name()
    last = fake.last_name()
    addr = fake.address()
    SQL_COMMAND = f"INSERT INTO person VALUES ('{first}', '{last}', '{addr}')"
    cursor.execute(SQL_COMMAND)

conn.commit()
conn.close()