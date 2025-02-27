#!/usr/bin/python3
"""Script that changes the name of a State object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a new database engine with the provided credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()
    # Update the state name to "New Mexico"
    state.name = "New Mexico"
    session.commit()  # Commit the changes to the database
