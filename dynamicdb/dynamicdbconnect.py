import sqlite3


db_options = {
    1: "demo.db",
    2: "sample.db",
    3: "testdata.db"
}


print("Which DB do you want to connect to?")
for key, value in db_options.items():
    print(f"{key}: {value}")


choice = int(input("Enter your choice (number): "))


selected_db = db_options.get(choice)

if selected_db:

    conn = sqlite3.connect(selected_db)
    print(f"Database '{selected_db}' connected.\n")
else:
    print("Invalid choice. Exiting.")


