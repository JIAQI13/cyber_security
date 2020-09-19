import xlrd, itertools

connector = ['%','$','_','*']
with xlrd.open_workbook('triatheles.xlsx') as wb:
    sh = wb.sheet_by_index(0)
    for row in range(sh.nrows):
        first_name = sh.row(row)[0].value
        last_name = sh.row(row)[1].value
        first_names = [first_name.lower(), first_name.upper(), first_name[0].upper() + first_name[1:].lower()]
        last_names = [last_name.lower(), last_name.upper(), last_name[0].upper() + last_name[1:].lower()]
        for v in itertools.product(first_names, connector, last_names):
            name = ''.join(v)
            print(name)