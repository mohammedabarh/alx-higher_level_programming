#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
with safe filtering against SQL injection
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

    # Create cursor and execute query with safe parameter binding
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close database connections
    cur.close()
    db.close()
