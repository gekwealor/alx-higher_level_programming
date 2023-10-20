#!/usr/bin/python3
"""script that lists all State objects that,
    contain the letter a from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Set up the tables in the database
    Base.metadata.create_all(engine)
    # Configuring session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query all instance that containe the letter a
    instance = session.query(State).filter(State.name.like('%a%')).all()
    for state in instance:
        print("{}: {}".format(state.id, state.name))
    session.close()
