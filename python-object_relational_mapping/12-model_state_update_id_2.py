#!/usr/bin/python3
"""
This is a script that changes the name of a State object
from the database hbtn_0e_6_usa
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
        state = session.query(State).filter(State.id == 2).first()
        state.name = "New Mexico"

        session.commit()

    session.close()
