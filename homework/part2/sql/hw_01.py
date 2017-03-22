import sqlite3

with sqlite3.connect("cars.db") as connection :
    c = connection.cursor()

    c.execute("DROP TABLE if exists inventory")
    c.execute("CREATE TABLE inventory(make text, model text, quantity int)")
