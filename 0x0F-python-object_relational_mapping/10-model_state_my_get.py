#!/usr/bin/python3
===
   Script that prints the state object with,
   name passed as arguments from database hbtn_0e_6_usa
===

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    """ Uses a cursor object to query"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(


