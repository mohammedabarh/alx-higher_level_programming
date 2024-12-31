#!/usr/bin/python3
"""Script that deletes all State objects with a name containing the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create a new database engine using provided credentials
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects with names containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    # Delete each state object retrieved from the query
    for state in states:
        session.delete(state)
    session.commit()  # Commit the changes to the database
