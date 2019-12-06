import xlrd
from den import all
from pdf import creatpdf


# Give the location of the file
loc = ("makeaton.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# For row 0 and column 0

for i in range(1, 80):
    name = sheet.cell_value(i, 0).title()
    # roll = str(int(sheet.cell_value(i, 5)))
    # # roll = str(sheet.cell_value(i, 5))
    # branch = sheet.cell_value(i, 4)
    # fileid = sheet.cell_value(i, 3)[33:]
    print(name)
    # path = all(name, fileid)
    # # path = "/Users/apple/Developer/id card/Driver/photo/Risheth Sunil.jpg"
    # creatpdf(i, name, roll, branch, path)

    # os.remove("certificate/certificate.")
