from dynamicdbconnect import *
# import sqlite3
# conn=sqlite3.connect('demo.db')

conn.execute('''create table student
(id int primary key not null,
rollno text not null,
name text not null,
marks text not null) ''')

print('table created')

conn.close()