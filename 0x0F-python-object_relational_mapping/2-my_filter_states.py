#!/usr/bin/python3
"""
Lists values in the states tables of a database where name
matches the argument
"""
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user="root", passwd="1914Jr@!",
            db="hbtn_0e_0_usa":)

    values = db.cursor()
    values.execute("SELECT * \
            FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS = '{}';")
    states = values.fetchall()

    for state in states:
        print(state)
