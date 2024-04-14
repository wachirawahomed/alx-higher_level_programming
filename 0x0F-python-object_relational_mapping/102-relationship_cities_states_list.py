#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
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

    # Query all City objects with their corresponding State object
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()

