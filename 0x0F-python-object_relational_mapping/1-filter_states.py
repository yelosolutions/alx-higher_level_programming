#!/usr/bin/python3
"""
Lists states with names starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd="1914Jr@!",
                         db=sys.argv[3], port=3306)

    c = db.cursor()
    c.execute("""SELECT * \
            FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS \
            LIKE 'N%';""")
    states = c.fetchall()

    for state in states:
        print(state)
