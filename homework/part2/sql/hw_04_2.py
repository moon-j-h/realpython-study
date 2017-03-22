"""Realpython part 2 sql homeword 4th
sql function : count()"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT make, model, quantity FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1])
        print(r[2])

        c.execute("SELECT count(order_date) FROM orders WHERE make=? AND model=?", (r[0], r[1]))

        result = c.fetchone()
        print(result[0])
        print()

