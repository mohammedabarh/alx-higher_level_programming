#!/usr/bin/python3
"""Script that prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query to fetch and print cities with their state names
    try:
        results = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()
        for city, state in results:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
