#!/usr/bin/python3
"""
Script that prints the first State object from
the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

