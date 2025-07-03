#!/usr/bin/python3
"""
This is a script that prints the State object
with the name passed as an argument
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database))

    with Session(engine) as session:
        state = session.query(State).filter(State.name == state_name).first()

        if state is None:
            print("Not found")
        else:
            print(state.id)

    session.close()
