#!/usr/bin/python3
"""
This is a script that lists all states with a name starting with
an N (uppercase N) from the database hbtn_0d_usa
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
    cursor.execute("SELECT * FROM states WHERE name LIKE "
                   "BINARY 'N%' ORDER BY id ASC")
    # LIKE is used for pattern matching
    # BINARY - ensures it'll stick to case-sensitive requirements
    # 'N%' means starts with N - % is a wildcard that matches any
    # sequence of characters

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    connection.close()
