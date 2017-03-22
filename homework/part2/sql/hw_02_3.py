"""Realpython part 2 sql homeword 2nd
sql select where"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT make, model, quantity FROM inventory WHERE make = 'Ford'")

    rows = c.fetchall()

    for row in rows:
        print(row)