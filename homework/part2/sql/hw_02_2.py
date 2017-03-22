"""Realpython part 2 sql homeword 2nd
sql update"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE inventory SET quantity=3 WHERE model='Ranger'")
    c.execute("UPDATE inventory SET quantity=13 WHERE model='Accord'")

    c.execute("SELECT make, model, quantity FROM inventory")
    rows = c.fetchall()

    for row in rows:
        print(row)
