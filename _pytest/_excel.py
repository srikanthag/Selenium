import xlrd

def read_locators(pagename):
    workbook = xlrd.open_workbook(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\_pytest\Objects.xls")
    worksheet = workbook.sheet_by_name(pagename)
    rows = worksheet.get_rows()
    headers = next(rows)
    return {row[0].value: (row[1].value, row[2].value) for row in rows}

login = read_locators("loginpage")
reg = read_locators("registrationpage")
home = read_locators("homepage")

print(login)
print(reg)




