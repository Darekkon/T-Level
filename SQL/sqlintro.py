'''
project: Introduction to using SQL development
'''

import sqlite3 as sq
conn = sq.connect('firstDB.sql')
conn.close()