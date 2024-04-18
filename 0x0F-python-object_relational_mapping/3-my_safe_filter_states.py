#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, using parameterized queries
to prevent SQL injection.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states from
    the database.
    """
    # Check if correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: {} username password database state_name"
              .format(argv[0]))
        exit(1)

    # Get MySQL credentials and state name from command line arguments
    username, password = argv[1], argv[2]
    database, state_name = argv[3], argv[4]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Create SQL query with parameterized query
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    # Execute SQL query with state_name as parameter
    cur.execute(sql_query, (state_name,))

    # Fetch all rows and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)
