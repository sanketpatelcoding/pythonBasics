from connectDb import *
# import sqlite3
# conn=sqlite3.connect('demo.db')

conn.execute('''create table drains
(id int primary key not null,
rivername text not null,
drainstatus text not null,
city text not null) ''')

print('table created')

conn.close()