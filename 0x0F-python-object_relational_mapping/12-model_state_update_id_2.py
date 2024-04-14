#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Updates a State object on the database.
    """

    username, password, database = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close session
    session.close()

