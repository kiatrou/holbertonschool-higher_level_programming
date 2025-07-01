#!/usr/bin/python3
"""
This is a script that lists all cities from the database hbtn_0d_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = ("SELECT cities.id, cities.name, states.name FROM cities JOIN "
             "states ON cities.state_id = states.id ORDER BY cities.id ASC")
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
