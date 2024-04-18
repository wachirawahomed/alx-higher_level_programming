#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create cursor object
    cur = db.cursor()

    # Execute SQL query to select states with the given name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
                .format(state_name))

    # Fetch all the rows and print them
    for row in cur.fetchall():
        print(row)
