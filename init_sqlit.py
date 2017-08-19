#coding:utf-8

import sqlite3

con = sqlite3.connect('movies.db')
cur = con.cursor()

try:
    cur.execute('CREATE TABLE movies(id integer PRIMARY KEY AUTOINCREMENT, name text, type text, actress text);')
    con.commit()
except Exception as e:
    print e

cur.close()
con.close()
