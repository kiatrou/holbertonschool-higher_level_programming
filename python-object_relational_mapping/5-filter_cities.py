#!/usr/bin/python3
"""
This is a script that takes in the name of a state as an argument
and lists all cities of that state
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = ("SELECT cities.id, cities.name FROM cities JOIN states ON "
             "cities.state_id = states.id WHERE states.name = %s ORDER "
             "BY cities.id ASC")
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
