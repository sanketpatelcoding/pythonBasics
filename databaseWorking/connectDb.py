#1import db
#2 .connect(databasename)

import sqlite3

conn = sqlite3.connect('demo.db')
print('database connected')
