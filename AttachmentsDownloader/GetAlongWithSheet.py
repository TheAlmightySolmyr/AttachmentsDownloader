import openpyxl

class GetAlongWithSheet:
    def __init__(self, sheet_path):
        self.active_sheet = openpyxl.load_workbook(sheet_path).active
    
    def cell_value(self, row, column):
        return self.active_sheet.cell(row,column).value
    
    def cell_range(self, coord1, coord2):
        return self.active_sheet[coord1:coord2]
    
    def all_values_to_dict(self):
        result = {}
        for i in self.active_sheet.values:
            result.setdefault(i[0], i[1])
        return result