#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of a database where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database using command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object to execute queries
    cur = db.cursor()

    # Execute SELECT query with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(query.format(sys.argv[4]))

    # Fetch and print matching rows
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Close database connection
    cur.close()
    db.close()
