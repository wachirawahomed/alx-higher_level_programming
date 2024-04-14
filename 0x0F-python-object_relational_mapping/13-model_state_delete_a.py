#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    deletes a State object on the database.
    """

    username, password, database = sys.argv[1:]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all)

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()

