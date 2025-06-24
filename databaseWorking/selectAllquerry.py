from connectDb import conn


# cursor = conn.cursor()
cursor=conn.execute("select * from drains")

#
# rows = cursor.fetchall()
#
# # Print each row
# for row in rows:
#     print(row)

for i in cursor:
    # print('id', i[0])
    # print('name', i[1])
    # print('drainstatus', i[2])
    # print('city', i[3], '\n')
    print(i,'\n')

# Close the connection
conn.close()
print('db closed')





