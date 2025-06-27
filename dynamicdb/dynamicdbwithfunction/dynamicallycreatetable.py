import sqlite3

conn = sqlite3.connect("abc.db")
cursor = conn.cursor()


tablename = input("Enter table name u want: ")

num_columns = int(input("How many columns? "))

print(f"u selectd {num_columns}")
columns = []
for i in range(num_columns):
    col_name = input(f"Enter colum name {i+1}: ")
    col_type = input(f"Enter type  {i+1}  ")
    columns.append(f"{col_name} {col_type}")

#here reference taken from net
columnssql = ", ".join(columns)
createtablesql = f"CREATE TABLE IF NOT EXISTS {tablename} ({columnssql});"
#CREATE TABLE IF NOT EXISTS table_name (    column1 datatype [constraints],    column2 datatype [constraints],    ...);


cursor.execute(createtablesql)
conn.commit()
print(f"Table '{tablename}' is created")


conn.close()

#key point range