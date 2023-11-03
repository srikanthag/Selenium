import openpyxl

path = r"C:\Users\srikanth\Desktop\IT\Testing\selenium_tutorial\Data_driven_testing\Data_2.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1,6):    #create 5 rows
    for c in range(1, 4):    #Create 3 colums
        sheet.cell(row=r,column=c).value="welcome"
workbook.save(path)







