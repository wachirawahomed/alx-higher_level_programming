#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

	username, password, database = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and order by id
    cities = session.query(State, City).join(City).order_by(City.id).all()

    # Print results
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()

