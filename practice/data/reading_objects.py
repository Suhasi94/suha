import xlrd

path = r"C:\Users\User\Desktop\locators_file.xlsx"

def read_locators():
    work_book = xlrd.open_workbook(path)
    work_sheet = work_book.sheet_by_name("LoginPage")
    row = work_sheet.get_rows()
    print(row)

    #for i in row:
        #print(i[0].value)

    #to skip the headers
    headers = next(row)
    #to print all the values
    #for i in row:
        #print(i[0].value, i[1].value, i[2].value, sep="---")
    #d = {}
    #for i in row:
        #d[i[0].value] = (i[1].value, i[2].value)

    #return d

    #dict_compreshension
    print({i[0].value:(i[1].value, i[2].value) for i in row})
read_locators()