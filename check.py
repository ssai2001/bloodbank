import openpyxl

workbook = openpyxl.load_workbook('static/export1.xlsx')
sheet = workbook.active

cell_object = sheet.cell(row=1,column=1)
print(cell_object.value)

# sheet.delete_rows(idx=1)
# workbook.save('static/export1.xlsx')