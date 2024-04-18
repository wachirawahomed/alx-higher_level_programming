#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query to select states with the given name
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY "
                   "%s ORDER BY id", (state_name,))

    # Fetch all the rows and print them
    for row in cursor.fetchall():
        print(row)
