#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
SQL injection safe!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query to get cities for the specified state, sorted by cities.id
    # Using parameterized query to prevent SQL injection
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and display results
    results = cursor.fetchall()
    city_names = []
    for row in results:
        city_names.append(row[1])  # row[1] is the city name
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
