#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database.
Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State).filter(State.name.like('%a%')).all()
        count = len(states)
        for state in states:
            session.delete(state)

        session.commit()
        print(f"Deleted {count} state(s).")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
