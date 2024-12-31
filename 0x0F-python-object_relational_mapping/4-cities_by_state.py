#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
with their corresponding state names
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

    # Create cursor and execute join query
    cur = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and display results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close database connections
    cur.close()
    db.close()
