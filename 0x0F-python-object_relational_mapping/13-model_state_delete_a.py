#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a new database engine using provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects with names containing the letter 'a'
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)  # Delete the state object
    session.commit()  # Commit the changes to the database
