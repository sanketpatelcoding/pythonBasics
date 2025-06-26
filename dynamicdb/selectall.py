from dynamicdbconnect import *

cursor = conn.cursor()

while True:
    check = input("Check student record? (1. yes / 2. no): ")

    if check == '1':
        id_val = input("Enter ID to view: ")

        cursor.execute("SELECT * FROM student WHERE id = ?", (id_val,))
        record = cursor.fetchone()

        if record:
            print(f"ID: {record[0]}, Roll No: {record[1]}, Name: {record[2]}, Marks: {record[3]}")
        else:
            print("No student found with this ID.")
    else:
        break

while True:
    check = input("Check all student records? (1. yes / 2. no): ")

    if check == '1':
        cursor.execute('SELECT * FROM student')
        records = cursor.fetchall()

        if records:
            print("\nAll Student Records:")
            print("ID\tRoll No\t\tName\t\tMarks")

            for rec in records:
                print(f"{rec[0]}\t{rec[1]}\t{rec[2]}\t{rec[3]}")
        else:
            print("No records found.")
    else:
        break

conn.close()
