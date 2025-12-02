import openpyxl


def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    rows = []
    for row in sheet.iter_rows(values_only=True):
        rows.append(row)

    header = rows[0]  # first row as header
    data_rows = []

    for row in rows[1:]:
        data_rows.append(dict(zip(header, row)))

    return data_rows
