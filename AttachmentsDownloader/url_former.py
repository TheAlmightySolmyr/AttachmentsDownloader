from GetAlongWithSheet import GetAlongWithSheet as gs

def form_url(sheet_path, domain=None):
    table = gs(sheet_path)
    iterable = len(table.to_list())
    result = []
    for i in range(iterable):
        url = table.cell_value(i+1, 1)
        if domain:
            url = f"{domain}{url}"
        result.append(url)
    return result