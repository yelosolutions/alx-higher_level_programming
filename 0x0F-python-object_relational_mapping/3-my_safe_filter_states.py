#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument in a safe way
Usage: ./3-my_safe_filter_sates.py <mysql username> \
        <mysql password> \
        <mysql database> \
        <state name searched>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    city = db.cursor()
    city.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = city.fetchall()

    for state in states:
        print(state)
