#!/usr/bin/python3
"""
Script that deletes all State objects with name containing letter 'a'
from the database hbtn_0e_6_usa.

Usage: ./13-model_state_delete_a.py <mysql username> \
                                   <mysql password> \
                                   <database name>
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()
    Base.metadata.create_all(engine)

    # Delete states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit changes and close session
    session.commit()
    session.close()
