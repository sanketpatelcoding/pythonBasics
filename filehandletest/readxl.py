import openpyxl


workbook = openpyxl.load_workbook('example.xlsx')


sheet = workbook['Sheet1']


for row in sheet.iter_rows(values_only=True):
    print(row)
