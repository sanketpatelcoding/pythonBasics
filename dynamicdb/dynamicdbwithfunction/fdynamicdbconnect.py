import os
import sqlite3

def list_databases():
    return [f for f in os.listdir() if f.endswith(".db")]

def select_or_create_database():
    while True:
        dbs = list_databases()

        if dbs:
            print("\nAvailable dbs:")
            for idx, db_name in enumerate(dbs, start=1):
                print(f"{idx}: {db_name}")
            print(f"{len(dbs)+1}: Create a new database")
        else:
            print("No databases  You hv to create nu.")
            return create_new_database()

        choice = input("Select db  number: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(dbs):
                selected_db = dbs[choice - 1]
                print(f"Connected to '{selected_db}'.\n")
                return sqlite3.connect(selected_db)
            elif choice == len(dbs) + 1:
                return create_new_database()
        print("Invalid choice. Try again.")

def create_new_database():
    name = input("Enter new database name (without .db): ").strip()
    if not name.endswith(".db"):
        name += ".db"
    open(name, 'a').close()
    print(f"Database '{name}' created and connected.\n")
    return sqlite3.connect(name)


conn = select_or_create_database()
