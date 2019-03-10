import xlrd

file_loc="F:/Selenium/WorkBook.xlsx"
wb=xlrd.open_workbook(file_loc)
ws=wb.sheet_by_index(0)
cell_val=ws.cell_value(0,1)
print(cell_val)