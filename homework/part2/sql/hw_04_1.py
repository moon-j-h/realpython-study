"""Realpython part 2 sql homeword 4th
sql function : count()"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    count = {
        "Focus Count" : "SELECT count(make) FROM orders WHERE model='Focus'",
        "Civic Count" : "SELECT count(make) FROM orders WHERE model='Civic'",
        "Ranger Count" : "SELECT count(make) FROM orders WHERE model='Ranger'",
        "Accord Count" : "SELECT count(make) FROM orders WHERE model='Accord'",
        "Avenger Count" : "SELECT count(make) FROM orders WHERE model='Avenger'",
    }

    for key, value in count.items():
        c.execute(value)
        result = c.fetchone()
        print(key+" : "+str(result[0]))

