#!/usr/bin/python3
"""
  Script that takes an argument and queries a database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to a database and queries
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306, usr=username, pswd=password, db=database)
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
    '{}' ORDER BY id ASC".format(name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
