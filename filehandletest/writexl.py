import openpyxl

# Create a new workbook (or load an existing one)
workbook = openpyxl.Workbook()

# Select the first sheet (default is Sheet1)
sheet = workbook.active
sheet.title = "Sheet1"  # Optional: rename the sheet if needed

# Write some data into Sheet1
data = [
    ["Name", "Age", "City"],
    ["sap", 30, " sdss"],
    ["rere", 25, "sddsdsd"],
    ["bvbv", 35, "Cgo"]
]

# Writing the data to the sheet
for row in data:
    sheet.append(row)

# Save the workbook
workbook.save('example.xlsx')
