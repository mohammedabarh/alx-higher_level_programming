#!/usr/bin/python3
"""Lists all City objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using provided credentials.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    # Configure a session class bound to the engine.
    Session = sessionmaker(bind=engine)

    # Create a session instance for database operations.
    session = Session()

    # Query all City objects ordered by their IDs.
    for city in session.query(City).order_by(City.id):
        # Print city ID, name, and associated state name.
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
