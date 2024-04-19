#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   'N%' ORDER BY id")

    # Fetch all the rows and print them
    for row in cursor.fetchall():
        print(row)
