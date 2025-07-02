from GetAlongWithSheet import GetAlongWithSheet as gs

def form_url(sheet_path, domain):
    table = gs(sheet_path)
    iterable = len(table.to_list())
    result = []
    for i in range(iterable):
        result.append(f'{domain}{table.cell_value(i+1,1)}')
    return result