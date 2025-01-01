#!/usr/bin/python3
"""
Retrieves and prints all City objects from the database along with their states.
"""

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a database engine for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # C Configure a session class bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session instance for database operations
    session = Session()

    # Ensure all tables are created in the database
    Base.metadata.create_all(engine)

    # Query to join State and City, ordered by city ID
    cities = session.query(State, City).join(City).order_by(City.id)
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session to free resources
    session.close()
