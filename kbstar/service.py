import pandas as pd
import xlwings as xw
from kbstar.model import Model

class Service:
    def __init__(self):
        self._model = Model()

    def new_model(self, param):
        model = self._model
        model.context = './data'
        model.fname = param
        print(model.fname)
        wb = xw.Book(model.context + '/' + model.fname)
        sheet = wb.sheets['매매종합']
        row_num = sheet.range(1, 1).end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        raw_data = sheet[data_range] \
            .options(pd.DataFrame, index=False, header=True).value
        return raw_data

