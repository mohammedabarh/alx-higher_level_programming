#!/usr/bin/python3
"""
Fetches and displays all City objects from the database along with their states.
"""

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Configure a session class
    Session = sessionmaker(bind=engine)

    # Create a session instance
    session = Session()
    Base.metadata.create_all(engine)

    # Query to join State and City, ordered by city ID
    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session to free resources
    session.close()
