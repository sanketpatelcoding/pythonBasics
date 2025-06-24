# x='g2.txt'
# op='r'
# file = open(x, op)
# content = file.read()
# print(content)
# file.close()
# Predefined list of filenames
filenames = ["g1.txt", "g2.txt", "notes.txt"]

# Ask user to enter a filename
userinput = input("Enter the filename: ")


if userinput in filenames:

    operation = input("Enter file operation u want to do 'r' for read, 'w' for write: ")

    try:

        file = open(userinput, operation)
        print(f"File '{userinput}' opened successfully in '{operation}' mode.")

        if operation == 'r':
            print(file.read())

        file.close()
    except Exception as e:
        print(f"Error opening file: {e}")
else:
    print("Filename not found in the list.")

