"""Realpython part 2 sql homeword 3rd
sql join : select join"""

import sqlite3

with sqlite3.connect("cars.db") as connection: 
    c = connection.cursor()

    c.execute("SELECT i.make, i.model, i.quantity, o.order_date FROM inventory i, orders o WHERE i.make=o.make AND i.model=o.model ORDER BY i.make ASC, i.model ASC, order_date ASC")

    rows = c.fetchall()

    for row in rows :
        print("make : {}, mode : {}".format(row[0], row[1]))
        print("quantity : {}".format(row[2]))
        print("order_date : {}".format(row[3]))
        print()