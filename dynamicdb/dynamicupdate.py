# from dynamicdbconnect import *
#
# cursor = conn.cursor()
#
# while True:
#     print("\nUpdate student record:")
#     id_val = input("Enter ID of student to update: ")
#
#     new_rollno = input("New Roll No: ")
#     new_name = input("New Name: ")
#     new_marks = input("New Marks: ")
#
#     cursor.execute("""
#         UPDATE student
#         SET rollno = ?, name = ?, marks = ?
#         WHERE id = ?
#     """, (new_rollno, new_name, new_marks, id_val))
#
#     conn.commit()
#     print("Record updated.")
#
#     cont = input("Update another? (yes/no): ").strip().lower()
#     if cont != 'yes':
#         break
#
# conn.close()
# print("Connection closed.")

#querry with plcaeholder ,strip.lower


from dynamicdbconnect import *

cursor = conn.cursor()

while True:
    id_val = input("Enter student ID to update: ")

    cursor.execute("SELECT id FROM student WHERE id = ?", (id_val,))
    if cursor.fetchone():
        rollno = input("New Roll No: ")
        name = input("New Name: ")
        marks = input("New Marks: ")

        cursor.execute("UPDATE student SET rollno = ?, name = ?, marks = ? WHERE id = ?",
                       (rollno, name, marks, id_val))
        conn.commit()
        print("Record updated.")
    else:
        print("No student with that ID.")

    if input("Update another? (yes/no): ").lower() != 'yes':
        break

conn.close()
