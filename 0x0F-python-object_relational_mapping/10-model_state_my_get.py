#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name to search (str)
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

    username, password, database, state_name = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch State object with the given state name
    state = session.query(State).filter_by(name=state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")
