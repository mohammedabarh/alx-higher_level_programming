#!/usr/bin/python3
"""
Deletes all State objects with names containing the letter 'a'
from the database using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Instantiate a Session
    session = Session()
    Base.metadata.create_all(engine)
    # Query for State objects with 'a' in their name
    state_del = session.query(State).filter(State.name.like('%a%')).all()
    for delete in state_del:
        session.delete(delete)
    # Commit changes and close the session
    session.commit()
    session.close()
