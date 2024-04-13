#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    # Get MySQL credentials and database name from command line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Exct SQL query to select all cities and their corresponding state names
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all rows and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

