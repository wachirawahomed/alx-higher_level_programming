#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    username, password, database = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add new State object to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

