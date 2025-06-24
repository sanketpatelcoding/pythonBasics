import openpyxl


filename = input("Enter the Excel file name (with .xlsx extension): ")

try:

    workbook = openpyxl.load_workbook(filename)


    sheet = workbook['Sheet1']
    for row in sheet.iter_rows(values_only=True):
        print(row)

except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the file .")

