from Data import *
from Library import *


def read_locators(sheetname):
    """Returns a dictionary with field name as key and locator type and locator value as value (tuple)"""
    wb = xlrd.open_workbook(Config.OBJECTS_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    objects = { }
    for index in range(1, total_rows):
        row = ws.row_values(index)
        objects[row[0]] = (row[1], row[2])
    return objects  # dictionary

def read_headers(sheetname, testcase=None):
    """retuns the headers of the testcase in comma seprated string"""
    wb = xlrd.open_workbook(Config.DATA_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    for index in range(total_rows):
        row = ws.row_values(index)
        if row[0] == testcase:
            headers = ws.row_values(index-1, 2)
            return ",".join([header for header in headers if header])
        elif testcase == None:
            headers = ws.row_values(index)
            return ",".join([header for header in headers if header])

def read_data(sheetname, testcase):
    """Returns a list of tuples"""
    wb = xlrd.open_workbook(Config.DATA_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    final_data = [ ]
    for index in range(total_rows):
        row = ws.row_values(index)
        if row[0] == testcase:
            data = ws.row_values(index, 1)
            data = [ item for item in data if item ]
            if data[0].lower() == "yes":
                final_data.append(tuple(data[1:]))


    return final_data


def read_data_as_list(sheetname):
    wb = xlrd.open_workbook(Config.DATA_FILE_PATH)
    ws = wb.sheet_by_name(sheetname)
    total_rows = ws.nrows
    final_data = []
    for index in range(1, total_rows):
        row = ws.row_values(index)
        print(row)
        final_data.append(tuple(row))
    return final_data