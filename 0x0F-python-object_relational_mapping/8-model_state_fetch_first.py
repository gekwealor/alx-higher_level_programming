#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # create database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(argv[1], argv[2], argv[3])))
    # set up the tables in the database
    Base.metadata.create_all(engine)
    #configuring session
    Session.configure(bind=eng)
    session = Session()
    # Query the first instance of state
    instance = session.query(State).first()
    if instance:
        print(instance.id, instance.name, sep=": ")
    else:
        print("Nothing")
