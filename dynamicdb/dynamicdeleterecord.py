from dynamicdbconnect import *

cursor = conn.cursor()

while True:
    id_val = input("Enter student ID to delete: ")

    cursor.execute("select id from student WHERE id = ?", (id_val,))
    if cursor.fetchone():
        cursor.execute("delete from student WHERE id = ?", (id_val,))
        conn.commit()
        print("Record deleted.")
    else:
        print("No student with that ID.")

    if input("Delete another? (yes/no): ").lower() != 'yes':
        break

conn.close()
