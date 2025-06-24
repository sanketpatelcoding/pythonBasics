import csv
import os

# Predefined filenames
filenames = ["demo.csv", "g1.txt", "g2.txt"]


userinput = input("Enter the filename: ")


if userinput in filenames:
    while True:
        operation = input("Enter file operation mode r: ")
        if operation == 'r':
            break

    if operation == 'r':
        with open(userinput, mode='r') as csvFile:
            reader = csv.DictReader(csvFile)
            lineCount = 0
            for data in reader:
                if lineCount == 0:
                    print(f"{' '.join(data)}")
                print(f"{data['name']} {data['contact']} {data['role']}")
                lineCount += 1
            print('Total data :', lineCount)


    os.rename(userinput, 'employee.csv')


    os.unlink('employee.csv')

else:
    print("Filename not found in the list.")
