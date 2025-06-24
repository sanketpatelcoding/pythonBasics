import openpyxl

# Ask user to enter the Excel file name
filename = input("Enter the Excel file name (with .xlsx extension): ")

try:
    # Load the workbook
    workbook = openpyxl.load_workbook(filename)

    # Select the sheet named 'Sheet1'
    sheet = workbook['Sheet1']

    print("Names in Column A:")
    for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):
        name = row[0]
        if name is not None:
            print(name)

except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the file name and try again.")
