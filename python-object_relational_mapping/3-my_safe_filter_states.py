#!/usr/bin/python3
"""
This is a script that takes an argument and displays all values
in the states tables of hbtn_0d_usa where name matches the argument
and takes into account SQL injections
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
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER "
                   "BY id ASC", (state_name,))
    # %s is a placeholder (not Python string formatting!)
    # The second argument (state_name,) is a tuple of values
    # MySQLdb automatically escapes the values to prevent injection
    # Note the comma in (state_name,) - this makes it a tuple even
    # with one item

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    connection.close()
