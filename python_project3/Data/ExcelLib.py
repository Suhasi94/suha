import xlrd

def read_locators():

    workbook = xlrd.open_workbook(r'C:\Users\User\PycharmProjects\python_project3\Data\locators_file.xlsx')
    worksheet = workbook.sheet_by_index(0)
    rows = worksheet.get_rows()
    headers = next(rows)
    return {row[0].value:(row[1].value,row[2].value) for row in rows}

#print(read_locators())