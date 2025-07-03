#!/usr/bin/python3
"""
This is a script that lists all State objects from database
hbtn_0d_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database))

    with Session(engine) as session:
        all_states = session.query(State).order_by(State.id).all()

        for state in all_states:
            print(f"{state.id}: {state}")

    session.close()
