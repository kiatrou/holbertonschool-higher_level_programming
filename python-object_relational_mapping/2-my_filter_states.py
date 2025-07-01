#!/usr/bin/python3
"""
This is a script that takes an argument and displays all values
in the states tables of hbtn_0d_usa where name matches the argument
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
    # Using .format() to use user's input
    query = ("SELECT * FROM states WHERE name = BINARY '{}' ORDER BY "
             "id ASC").format(state_name)
    cursor.execute(query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
