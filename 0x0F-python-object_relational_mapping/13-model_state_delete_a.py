#!/usr/bin/python3
"""Script that deletes all State objects with names containing the letter 'a'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Set up the database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    
    # Delete the states and commit changes
    for state in states_to_delete:
        session.delete(state)
    session.commit()
