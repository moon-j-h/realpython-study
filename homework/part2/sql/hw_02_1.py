"""Realpython part 2 sql homeword 2nd
sql insert """

import sqlite3

with sqlite3.connect("cars.db") as connection: 
    c = connection.cursor()

    c.execute("INSERT INTO inventory(make, model, quantity) VALUES('Ford', 'Focus', 10)")
    c.execute("INSERT INTO inventory(make, model, quantity) VALUES('Ford', 'Civic', 12)")
    c.execute("INSERT INTO inventory(make, model, quantity) VALUES('Ford', 'Ranger', 14)")
    c.execute("INSERT INTO inventory(make, model, quantity) VALUES('Honda', 'Accord', 9)")
    c.execute("INSERT INTO inventory(make, model, quantity) VALUES('Honda', 'Avenger', 23)")
