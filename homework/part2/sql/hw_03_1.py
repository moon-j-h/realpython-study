"""Realpython part 2 sql homeword 3rd
sql join : create another table"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

    orders = [
        ('Ford', 'Focus','2017-03-22'),
        ('Ford', 'Focus','2017-03-25'),
        ('Ford', 'Focus','2017-03-20'),
        ('Ford', 'Civic','2017-03-27'),
        ('Ford', 'Civic','2017-03-22'),
        ('Ford', 'Civic','2017-03-22'),
        ('Ford', 'Ranger','2017-03-20'),
        ('Ford', 'Ranger','2017-03-27'),
        ('Ford', 'Ranger','2017-03-23'),
        ('Honda', 'Accord','2017-03-22'),
        ('Honda', 'Accord','2017-03-20'),
        ('Honda', 'Accord','2017-03-21'),
        ('Honda', 'Avenger','2017-03-25'),
        ('Honda', 'Avenger','2017-03-22'),
        ('Honda', 'Avenger','2017-03-27'),
    ]

    c.executemany("INSERT INTO orders(make, model, order_date) VALUES(?, ?, ?)", orders)
    