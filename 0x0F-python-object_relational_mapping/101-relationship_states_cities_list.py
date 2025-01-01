#!/usr/bin/python3
"""Lists all State objects and their corresponding City objects."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using provided credentials.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Configure a session class bound to the engine.
    Session = sessionmaker(bind=engine)

    # Create a session instance for database operations.
    session = Session()

    # Query all State objects ordered by their IDs.
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

        # Print corresponding City objects for each State.
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
