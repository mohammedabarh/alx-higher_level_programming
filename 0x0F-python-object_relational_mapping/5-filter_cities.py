#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state
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

    # Create cursor and execute filtered join query
    cur = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))

    # Fetch results and format output
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))

    # Close database connections
    cur.close()
    db.close()
