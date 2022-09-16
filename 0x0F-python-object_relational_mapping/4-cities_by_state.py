#!/usr/bin/python3
"""
List all cities from a database hbtn_0e_0_usa oredered by city id
Usage: ./4-cities_by_state <mysql username> \
        <mysql password> \
        <database name> \
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.id \
                 ORDER BY `c`.id;")
    states = c.fetchall()

    for state in states:
        print(state)
