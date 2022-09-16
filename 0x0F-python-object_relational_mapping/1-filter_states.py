#!/usr/bin/python3
"""
Lists all states with N from the database hbtn_0e_0_usa
Usage: ./1-filter_states <mysql username> \
        <mysql password> \
        <mysql database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    states = c.fetchall()

    for state in states:
        if state[1][0] == "N":
            print(state)
