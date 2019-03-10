import xlrd

file_loc="C:/Users/ADMIN/PycharmProjects/13th_Class_9_3_2019/Files/WorkBook.xlsx"
wb=xlrd.open_workbook(file_loc)
ws=wb.sheet_by_index(0)
cell_val=ws.cell_value(0,1)
print(cell_val)