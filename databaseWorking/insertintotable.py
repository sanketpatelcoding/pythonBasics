# from connectDb import *
#
# # remember
# #.connect to connect for sqlite3 like drivermanager
# #table creation and insert can be done with .execute
#
from connectDb import *

conn.execute("INSERT INTO drains VALUES (3, 'g', 'h', 'i')")
conn.commit()
print('Data inserted')
conn.close()
print('closed db connection')
