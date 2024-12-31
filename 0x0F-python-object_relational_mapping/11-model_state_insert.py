#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create a new database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)  # Add the new state to the session
    session.commit()  # Commit the transaction to the database
    print(new_state.id)  # Print the id of the new state
