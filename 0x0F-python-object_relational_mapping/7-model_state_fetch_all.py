#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch all State objects
    all_states = session.query(State).order_by(State.id).all()

    for state in all_states:
        print("{}: {}".format(state.id, state.name))

