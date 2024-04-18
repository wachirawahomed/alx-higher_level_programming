#!/usr/bin/python3
"""
Script that lists all cities of a specific state from
the database hbtn_0e_4_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish connection to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Prepare SQL query
    query = "SELECT cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id"

    # Execute SQL query with state name as parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Print cities separated by comma
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print("")
