from connectDb import *

cursor = conn.execute("select * from drains where id='2'")

for i in cursor:
    print(i)


conn.close()
print('db closed')
