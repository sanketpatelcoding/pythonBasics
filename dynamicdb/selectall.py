from dynamicdbconnect import *

cursor = conn.cursor()

while True:
    check = input("check student record? (1.yes and 2. no): ")

    if check == '1':
        id_val = input("Enter ID to view: ")

        cursor.execute("select * from student where id = ?", (id_val,))
        record = cursor.fetchone()

        if record:
            print(f"iD: {record[0]}, roll num: {record[1]}, name: {record[2]}, Marks: {record[3]}")
        else:
            print("No student of this id.")
    else:
        break

conn.close()
