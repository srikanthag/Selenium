import smoke as smoke
import xlrd

from _pytest.test_login import test_login


def read_header(sheetname, testcase):
    workbook = xlrd.open_workbook(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\_pytest\testcases.xlsx")
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    for rowno, row in enumerate(rows):
        if row[0] == testcase:
            temp_data = worksheet.row_values(rowno-1, start_colx=2)
            data = [item for item in temp_data if item]
            return ''.join(data)

















