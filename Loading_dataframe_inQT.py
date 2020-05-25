import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import pickle
import Xls_to_dataframe
from Xls_to_dataframe import *



def read_pickle(): #Add in a parameter for the file name
    infile = open(r"G:\Staff Programs\Digital\Automates\Working\Automation Hackathon\2020\Idea 1 - Code Databasing\PKL files\code_db.pkl","rb" )
    document_info = pickle.load(infile)
    print(document_info)
    infile.close
    return document_info

##df = pd.DataFrame({'a': ['Mary', 'Jim', 'John'],
##                   'b': [100, 200, 300],
##                   'c': ['a', 'b', 'c']})


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #model = pandasModel(read_pickle())
    dfs = excel_read() # a dictionary of dataframes
    for i in dfs:
        model = pandasModel(dfs[i])
        view = QTableView()
        view.setModel(model)
        view.resize(800, 600)
        view.show()
    
    sys.exit(app.exec_())
    






