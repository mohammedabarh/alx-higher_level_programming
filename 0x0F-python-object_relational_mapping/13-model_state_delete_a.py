#!/usr/bin/python3
"""
Deletes all State objects containing letter 'a' from database.
Script uses SQLAlchemy module for database operations.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Configure database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Initialize session factory
    Session = sessionmaker(bind=engine)

    # Create database session
    session = Session()
    Base.metadata.create_all(engine)

    # Query and delete states containing letter 'a'
    state_del = session.query(State).filter(State.name.like('%a%')).all()
    for delete in state_del:
        session.delete(delete)

    # Persist changes and cleanup
    session.commit()
    session.close()
