from dynamicdbconnect import *

cursor = conn.cursor()

while True:
    print("\nEnter student details:")
    idval = int(input("iD: "))
    rollno = input("roll no: ")
    name = input("mnme: ")
    marks = input("mark: ")

    cursor.execute(
        "INSERT INTO student (id, rollno, name, marks) VALUES (?, ?, ?, ?)",
        (idval, rollno, name, marks)
    )
    conn.commit()
    print("Record inserted.")

    cont = input("Do you want to insert another record? (yes/no): ").strip().lower()
    if cont != 'yes':
        break
#if cont !='yes' taken from refernce
conn.close()
print("Connection closed.")
