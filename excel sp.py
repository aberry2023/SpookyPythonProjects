import xlrd as xl

loc = "C:\Users\13139\censuspopdata.xlsx"

wb = xl.open_workbook(loc)
s1 = wb.sheet_by_index(0)
s1.cell_value(0, 0)

print("No. of rows:", s1.nrows)
print("No. of columns:", s1.ncols)
