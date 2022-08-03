import xlrd

#open workbook
#interact with sheets
#get the data from the rows and interact with cells

def read_locators():
    workbook = xlrd.open_workbook(r"C:\Users\User\Desktop\locators_file.xlsx")
    worksheet = workbook.sheet_by_index(0)
    rows = worksheet.get_rows()
    '''
    for row in rows:
        print(row)
    
    headers = next(rows)
    for row in rows:
        print(row[0].value,row[1].value,row[2].value,sep="---")
    '''
    #store the data in the form of dictionary
    headers = next(rows)
    '''
    d = {}
    for row in rows:
        d[row[0].value] = (row[1].value,row[2].value)
    return d
    '''
    #dictionary comprehension
    return {row[0].value:(row[1].value,row[2].value) for row in rows}

print(read_locators())