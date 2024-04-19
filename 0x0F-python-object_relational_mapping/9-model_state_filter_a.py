#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch State objects containing letter 'a'
    s = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print results
    for state in s:
        print("{}: {}".format(state.id, state.name))
