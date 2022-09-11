#!/usr/bin/python3
"""
List all cities of state
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    city = db.cursor()
    city.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states ON cities.state_id = states.id \
                 WHERE states.name = '{}';".format(sys.argv[4]))
    states = city.fetchall()

    print(", ".join([state[1] for state in states]))
