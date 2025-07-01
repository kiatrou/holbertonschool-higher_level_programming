#!/usr/bin/python3
"""
This is a script that lists all states from the database hbtn_0d_usa
"""


import MySQLdb
import sys


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

# Makes sure the file only runs when executed
if __name__ == "__main__":

    # Cursor - acts as a pointer that lets you execute SQL commands and navigate through results. This is what sends SQL commands to the database
    cursor = connection.cursor()
    # SQL Query - Selects all the states and orders them in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches and displays the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up resources - do this to avoid memory leaks and leaving the database in an unstable state
    # Closing the cursor frees up resources and tells the database you're done with this particular query session
    cursor.close()
    # Closing the connection to the MySQL server, freeing up the connection slot for other programs to use
    connection.close()
