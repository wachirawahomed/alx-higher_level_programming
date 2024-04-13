#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states from the database.
    """
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
            passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute SQL query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

