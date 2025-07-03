#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
Results are sorted by cities.id in ascending order
Format: <state name>: (<city id>) <city name>
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities with their states, sorted by cities.id
    cities = session.query(City, State)\
             .join(State, City.state_id == State.id)\
             .order_by(City.id)\
             .all()

    # Print results in the required format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
