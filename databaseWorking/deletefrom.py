from fileinput import close

from connectDb import  conn

conn.execute("delete from drains where id='3'")
conn.commit()

print('after delete')

conn.execute("update drains set drainstatus = 'cleaned' where id = 2")
conn.commit()
cursor=conn.execute("select * from drains")
for i in cursor:
    print(i,' ')

conn.close()
print('db s clodes')