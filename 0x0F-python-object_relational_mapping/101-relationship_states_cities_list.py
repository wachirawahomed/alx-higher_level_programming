#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close session
    session.close()

