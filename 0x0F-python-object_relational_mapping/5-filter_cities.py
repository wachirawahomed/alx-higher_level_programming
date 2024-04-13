#!/usr/bin/python3
"""
This script lists all cities of the specified state
from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """
    # Check if correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: {} username password database state_name"
              .format(argv[0]))
        exit(1)

    # Get MySQL credentials, database name, and state name from
    # command line arguments
    username, password, database, state_name = argv[1], argv[2]
    database, state_name = argv[3], argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select all cities of the specified state
    cur.execute("""
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch and print the result
    result = cur.fetchone()[0]
    if result:
        print(result)

