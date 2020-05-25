################################################################

# https://pythonprogramminglanguage.com/pyqt-combobox/
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QMessageBox
from PyQt5.QtCore import QSize, QRect    

        
class ComboBoxs(QWidget):
   def __init__(self, tables,parent = None):
      super(ComboBoxs, self).__init__(parent)
      
      layout = QtWidgets.QHBoxLayout()
      self.cb = QtWidgets.QComboBox()
      self.cb.addItems(tables)
      self.cb.currentIndexChanged.connect(self.table_view)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setMinimumSize(QSize(100, 100))    #Sizing the application
      self.setWindowTitle("Table List")
   #https://pythonprogramminglanguage.com/pyqt5-message-box/

   def table_view(self):
        print("Tables in the database: ")
        for tbname_index in range(self.cb.count()):
            print (self.cb.itemText(tbname_index))
        text = "The selected table is: ",self.cb.currentText()
        #k.append(text)
        #print(text)
        #QMessageBox.about(self, "Current table", text)
        print ("The selected table is: ",self.cb.currentText())
        #return self.cb.currentText()

    

        
      
		
def main():
   app = QtWidgets.QApplication(sys.argv)
   ex = ComboBoxs(['1','2','3','4'])
   ex.show()
   #sys.exit(app.exec_())

#if __name__ == '__main__':
#main()     




   

################################################################
