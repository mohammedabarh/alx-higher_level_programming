#!/usr/bin/python3
"""
This script removes all State objects from the database
where the name contains the letter 'a'.
It utilizes the SQLAlchemy module.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Initialize the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Set up a session configuration class
    Session = sessionmaker(bind=engine)
    
    # Create a session instance
    session = Session()
    
    # Ensure the database schema is created
    Base.metadata.create_all(engine)
    
    # Query for all states containing 'a' in their name
    state_del = session.query(State).filter(State.name.like('%a%')).all()
    
    # Delete the selected state objects
    for delete in state_del:
        session.delete(delete)
    
    # Save changes to the database and close the session
    session.commit()
    session.close()
