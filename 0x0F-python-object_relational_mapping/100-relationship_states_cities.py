#!/usr/bin/python3
"""
Script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add new state and city
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)

    # Commit changes
    session.commit()

    # Close session
    session.close()

