#!/usr/bin/python3

import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user="root", db="hbtn_0e_0_usa", password="1914Jr@!", host="localhost")

    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    states = c.fetchall()

    for state in states:
        print(state)
