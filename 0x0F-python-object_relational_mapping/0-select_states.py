#!/usr/bin/python3
"""
  This script prints states from a database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ Uses a cursor object to query"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=dbname, charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    # HERE I have to know SQL to grab all states in my database

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
