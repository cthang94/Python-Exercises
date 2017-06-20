import openpyxl

workbook = openpyxl.load_workbook("example.xlsx")
sheet = workbook.get_sheet_by_name("Sheet1")
a = sheet.get_highest_row()
print(a)
