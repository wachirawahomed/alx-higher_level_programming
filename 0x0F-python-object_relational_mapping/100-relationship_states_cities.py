#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """
    username, password, database = sys.argv[1:]

    # Create engine to establish connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create all defined tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California state
    cali = State(name="California")
    session.add(cali)

    # Create San Francisco city
    sf = City(name="San Francisco", state=cali)
    session.add(sf)

    session.commit()
