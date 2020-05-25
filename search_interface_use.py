# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtCore import QSize, QRect 
import sys, os, io, csv
#import Database_Creator
#from Database_Creator import *
import database_class
from database_class import *
import Xls_to_dataframe
from Xls_to_dataframe import * #excel_read() using this function for receiving the user input
from tkinter import *
from tkinter import filedialog
import Database_Creator
from Database_Creator import *
from Directory_view_sample import *

from Stats_analysis import *
import sqlite3
import pandas as pd
#from directory_view_tkinter import *



        
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)         
        
        
        #self.initDb("Meggan_db.db")
        self.setupUi(self)  #Need to remove table view from the initial setupUI
        self.center()
        self.database = ""
        
        
   
    def initDb(self,dbname):
        fix_database = dbname.split(".")[0]
        print(fix_database)
        self.database = fix_database
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(dbname)
        db.setConnectOptions("QSQLITE_OPEN_READONLY=1")
        

        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\n" + str(db.lastError().text()),
                QMessageBox.Cancel)
            sys.exit()
        self.model = QSqlQueryModel()
            
              
     
    def closeEvent(self, event):       
        app = QApplication.instance()
        app.closeAllWindows()
        event.accept()
        
    def mousePressEvent(self, event):
        self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
        self.activateWindow()
        self.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1110, 730)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"C:\Users\Omar.Metwally\Documents\Python Scripts\Toronto Hackathon\pyqt-sqlite-interface\resources\1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout_search = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_search.setObjectName("verticalLayout_search")
        
        self.vertLayoutSearchPref = QtWidgets.QVBoxLayout()
        self.vertLayoutSearchPref.setObjectName("vertLayoutSearchPref")
        
        self.groupBoxSearchPref = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSearchPref.setObjectName("groupBoxSearchPref")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxSearchPref)
        self.gridLayout.setObjectName("gridLayout")
        
        self.sheetNumLabel = QtWidgets.QLabel(self.groupBoxSearchPref)
        self.sheetNumLabel.setObjectName("sheetNumLabel")
        self.gridLayout.addWidget(self.sheetNumLabel, 0, 0, 1, 1)
        
        self.sheetNumInputs = QtWidgets.QLineEdit(self.groupBoxSearchPref)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sheetNumInputs.sizePolicy().hasHeightForWidth())
        self.sheetNumInputs.setSizePolicy(sizePolicy)
        self.sheetNumInputs.setPlaceholderText("")
        self.sheetNumInputs.setClearButtonEnabled(True)
        self.sheetNumInputs.setObjectName("sheetNumInputs")
        self.sheetNumInputs.returnPressed.connect(self.searchAll)
        self.gridLayout.addWidget(self.sheetNumInputs, 0, 1, 1, 1)

        self.sheetNumSearchButton = QtWidgets.QPushButton(self.groupBoxSearchPref)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/256px-Magnifying_glass_icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sheetNumSearchButton.setIcon(icon1)
        self.sheetNumSearchButton.setObjectName("sheetNumSearchButton")
        self.sheetNumSearchButton.clicked.connect(self.searchAll)
        self.gridLayout.addWidget(self.sheetNumSearchButton, 0, 2, 1, 1)

        self.sheetNumLabel2 = QtWidgets.QLabel(self.groupBoxSearchPref)
        self.sheetNumLabel2.setObjectName("sheetNumLabel")
        self.gridLayout.addWidget(self.sheetNumLabel2, 1, 0, 1, 1)
        
        self.sheetNumInputs2 = QtWidgets.QLineEdit(self.groupBoxSearchPref)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sheetNumInputs2.sizePolicy().hasHeightForWidth())
        self.sheetNumInputs2.setSizePolicy(sizePolicy)
        self.sheetNumInputs2.setPlaceholderText("")
        self.sheetNumInputs2.setClearButtonEnabled(True)
        self.sheetNumInputs2.setObjectName("sheetNumInputs")
        self.sheetNumInputs2.returnPressed.connect(self.searchAll)
        self.gridLayout.addWidget(self.sheetNumInputs2, 1, 1, 1, 1)

        self.sheetNumSearchButton2 = QtWidgets.QPushButton(self.groupBoxSearchPref)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/256px-Magnifying_glass_icon.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sheetNumSearchButton2.setIcon(icon1)
        self.sheetNumSearchButton2.setObjectName("sheetNumSearchButton")
        self.sheetNumSearchButton2.clicked.connect(self.searchAll)
        self.gridLayout.addWidget(self.sheetNumSearchButton2, 1, 2, 1, 1)

        
        
        self.vertLayoutSearchPref.addWidget(self.groupBoxSearchPref)
        self.verticalLayout_search.addLayout(self.vertLayoutSearchPref)
        
        self.boxLayoutResults = QtWidgets.QVBoxLayout()
        self.boxLayoutResults.setObjectName("boxLayoutResults")
        self.groupBoxResults = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxResults.setObjectName("groupBoxResults")
        self.verticalLayout_table = QtWidgets.QVBoxLayout(self.groupBoxResults)
        self.verticalLayout_table.setObjectName("verticalLayout_table")


        ########################################################################################
        #This is for setting up the table view
        #Removing this leaves the area distorted when adding to the vertical Layout
        ########################################################################################
        
        self.tableView = QtWidgets.QTableView(self.groupBoxResults)
        self.tableView.setObjectName("tableView")
        #self.tableView.setModel(self.model) #for the table of the database to add in
        
        self.tableView.sortByColumn(0, 0)
        self.tableView.setSortingEnabled(True)
        self.tableView.resizeColumnsToContents()
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setCornerButtonEnabled(True)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setStyleSheet("QTableView::item:hover{background-color:#0abde3;}")
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableView.doubleClicked.connect(self.openSelectedDrawings)
        self.verticalLayout_table.addWidget(self.tableView)


        
        ########################################################################################
        
        self.horLayoutButtons = QtWidgets.QHBoxLayout()
        self.horLayoutButtons.setObjectName("horLayoutButtons")
        
        self.numResultsLabel = QtWidgets.QLabel(self.groupBoxResults)
        self.numResultsLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        #self.initNumResults = self.model.rowCount()
        #self.numberResultsLabelMessage(self.model.rowCount())
        self.numResultsLabel.setObjectName("numResultsLabel")
        self.horLayoutButtons.addWidget(self.numResultsLabel)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horLayoutButtons.addItem(spacerItem)

       
        ###################################################################################################
        #This is for seeing the student analysis 
        self.Analysis = QtWidgets.QPushButton(self.groupBoxResults)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/256px-Magnifying_glass_icon.svg - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Analysis.setIcon(icon2)
        self.Analysis.setObjectName("Student_Analysis")
        self.Analysis.clicked.connect(self.chartGenerator) #This is for connecting the resetted search to the bar
        self.horLayoutButtons.addWidget(self.Analysis)

        ###################################################################################################
        
        #This is for resetting the search connected to the reset search area
        self.resetSearch = QtWidgets.QPushButton(self.groupBoxResults)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/256px-Magnifying_glass_icon.svg - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetSearch.setIcon(icon2)
        self.resetSearch.setObjectName("resetSearch")
        self.resetSearch.clicked.connect(self.clearSearch) #This is for connecting the resetted search to the bar
        self.horLayoutButtons.addWidget(self.resetSearch)

        ###################################################################################################
        
        #This section is for adding the open button  for opening a table
        ###################################################################################################
        self.openSelected = QtWidgets.QPushButton(self.groupBoxResults)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Icon_open_file_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openSelected.setIcon(icon3)
        self.openSelected.setObjectName("openSelected")
        self.openSelected.clicked.connect(self.showTable) 
        self.horLayoutButtons.addWidget(self.openSelected)
        #####################################################################################################
        
        self.verticalLayout_table.addLayout(self.horLayoutButtons)
        self.boxLayoutResults.addWidget(self.groupBoxResults)
        self.verticalLayout_search.addLayout(self.boxLayoutResults)

        ######################################################################################################
        
        self.groupBoxResults.raise_()


        ######################################################################################################
        #Menu Window
        ######################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")

        ######################################################################################################
        #These are the menu headers

        #FILE
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        #DATABASE
        #New menu widget  for database information
        self.menu_Database = QtWidgets.QMenu(self.menubar) #Adding it to the menubar 
        self.menu_Database.setObjectName("Database")

        #DATA
        self.menu_Data = QtWidgets.QMenu(self.menubar)
        self.menu_Data.setObjectName("Data")
        
        
        #The HELP
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")

        #ANALYSIS
        ######################################################################################################
        
        
        self.menuCopy_Selected = QtWidgets.QMenu(self.menu_File)
        self.menuCopy_Selected.setObjectName("menuCopy_Selected")

        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.action_Quit = QtWidgets.QAction(MainWindow, shortcut="Ctrl+Q")
        self.action_Quit.setObjectName("action_Quit")
        
        self.action_Filter = QtWidgets.QAction(MainWindow)
        self.action_Filter.setObjectName("action_Filter")
        
        self.action_About = QtWidgets.QAction(MainWindow, triggered=self.about)
        self.action_About.setObjectName("action_About")
        
        self.actionCopy_Sheet_Number = QtWidgets.QAction(MainWindow, triggered=self.copySheetNumber)
        self.actionCopy_Sheet_Number.setObjectName("actionCopy_Sheet_Number")
        
        self.actionCopy_Row = QtWidgets.QAction(MainWindow, triggered=self.copySelected)
        self.actionCopy_Row.setObjectName("actionCopy_Row") 
        
        self.action_Refresh = QtWidgets.QAction(MainWindow, shortcut="F5", triggered=self.refresh)
        self.action_Refresh.setObjectName("action_Refresh")
        
        self.action_Search = QtWidgets.QAction(MainWindow)
        self.action_Search.setIcon(icon1)
        self.action_Search.setObjectName("action_Search")
        
        self.action_Help = QtWidgets.QAction(MainWindow, shortcut="F1", triggered=self.helpMessage)
        self.action_Help.setObjectName("action_Help")


        #####################################################################################################
        #Database Tools

        ##Creating a Database
        self.action_createDatabase = QtWidgets.QAction(MainWindow, triggered=self.createDB)
        self.action_createDatabase.setObjectName("menu_Create_Database")

        ##Opening a Database
        self.action_openDatabase = QtWidgets.QAction(MainWindow, triggered=self.openDB)
        self.action_openDatabase.setObjectName("menu_Open_Database")
        
        #####################################################################################################

        
        #####################################################################################################
        #Data Tools

        #Add Data
        self.action_addData = QtWidgets.QAction(MainWindow, triggered=self.addDB_Table)
        self.action_addData.setObjectName("Add Data")
        




        #####################################################################################################

        
        ######################################################################################################
        #Here for adding the different options to the menu headers on the taskbar
        
        ##Adding to the FILE functionalty to Menu headers
        self.menu_File.addAction(self.menuCopy_Selected.menuAction())        
        self.menu_File.addAction(self.action_Refresh)
        self.menu_File.addAction(self.action_Quit)
        self.menuCopy_Selected.addAction(self.actionCopy_Sheet_Number)
        self.menuCopy_Selected.addAction(self.actionCopy_Row)


        ##Adding to the HELP functionalty to Menu headers
        self.menu_Help.addAction(self.action_Help)
        self.menu_Help.addAction(self.action_About)


        ##Adding to the DATABASE functionalty to Menu headers
        self.menu_Database.addAction(self.action_createDatabase)
        self.menu_Database.addAction(self.action_openDatabase)


        ##Adding to the DATA functionality to Menu Headers
        
        self.menu_Data.addAction(self.action_addData)
        
        


        ######################################################################################################
        #For the adding the different menu headers on the taskbar
        self.menubar.addAction(self.menu_File.menuAction()) 
        self.menubar.addAction(self.menu_Database.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menubar.addAction(self.menu_Data.menuAction())


        ########################################################################################################

        
        self.retranslateUi(MainWindow)
        self.action_Quit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ######################################################################################################
    
    def about(self):
        QMessageBox.about(self, "About",
                "<b>Document Fitcher Tool</b><br>"
                "Version: 0.1 ")

    def helpMessage(self):
        QMessageBox.about(self, "Help",
                "<b>Support: </b> <a href='mailto:Felicity.Graves@arup.com; Gio.Harvey@arup.com; Omar.Metwally@arup.com; Pierre-Louis.Cons@arup.com; sebastien.cote@arup.com?subject=Document Fitcher Tool'>Email Us!</a>")
    
    def statusBarMessage(self, message):
        self.statusBar().showMessage(str(message) + " files")
        
    def numberResultsLabelMessage(self, message):
        self.numResultsLabel.setText(str(message) + " of " + str(self.initNumResults) + " files")
    
    def searchAll(self):     
        inputsSheetNum = self.sheetNumInputs.text()
        keywordsSheetNum = inputsSheetNum #Getting the the keyword from the sheet
        #matching_query = '''Select * From {0} Where ID = {1}'''.format('table_1',keywordsSheetNum)

        #Knowledge,Communication,Thinking,Application
        #When editing it out later

        
        #matching_query = ''' Select * From Knowledge_two as K JOIN {1} as T where K.ID = T.ID AND K.ID = {0}'''.format(keywordsSheetNum,self.tableName)
        specific_tables = ["Knowledge","Communication","Thinking","Application"]
       
        
        
        
        #matching_query = '''select Code_name, Art_Number, Art_Name, Content, Page, Commentary FROM search_articles
        #                        JOIN {0} ON search_articles.Art_Number = {0}.Number
        #                        WHERE search_articles MATCH '{1}' Order by bm25(search_articles,0,20,10); '''.format('table1',keywordsSheetNum)
    

        #self.model.setQuery(QSqlQuery(matching_query)) #old query

        #for table in specific_tables:
            #matching_query = '''Select * From {1} where ID = {0}'''.format(keywordsSheetNum,table)

        matching_query = '''Select K.*,C.*,T.*,A.* From Knowledge as K JOIN Communication as C JOIN Thinking as T JOIN Application as A where K.ID = C.ID and K.ID = T.ID and K.ID = A.ID and K.ID = {0}'''.format(keywordsSheetNum)
        self.model.setQuery(QSqlQuery(matching_query))

        
        #value = self.model.record(1).value(100000)
        #https://www.sqlitetutorial.net/sqlite-except/
        
       
        self.numberResultsLabelMessage(self.model.rowCount())


    ##########################################Choosing table############################################################
    def showTable(self): #Choosing from the list table

        table_list = table(self.database)
        tables = table_list.list_tables()
       
        OPTIONS = tables #etc

        master = Tk()
        master.geometry("400x200")

        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value

        opt = OptionMenu(master, variable, *OPTIONS)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")


        labelTest = Label(text="", font=('Helvetica', 12), fg='red')
        labelTest.pack(side="top")
        k = []

        def callback(*args):
            value = variable.get()
            result = value[1:len(value)-2]
            labelTest.configure(text="The selected table is {}".format(result))
            self.tableName = result #My chosen table 
            self.model.setQuery(QSqlQuery("select * from {}".format(result)))
        variable.trace("w", callback)

        mainloop()

     ###############################################################################################################       

    def openSelectedDrawings(self):
        i = self.tableView.selectionModel().selectedRows()
        for row in sorted(i):
            x = row.row()

            index = self.model.index(x, 8)
            filePath = self.model.data(index)

            #filePath = filePath.strip(" \t\n\r")      
            #filePath = r"C:\Users\Gio.Harvey\Documents\Mommy\pyqt-sqlite-interface"
            try:
                os.startfile(filePath)
                print(filePath)
            except Exception as e:
                if len(i) > 1:
                    QMessageBox.critical(None, "Error", "Cannot open selected Article",
                    QMessageBox.Cancel)
                else:
                    QMessageBox.critical(None, "Error", "Cannot open selected Article",
                    QMessageBox.Cancel)
    ###############################################################################################################
          
    def copySelected(self):
        i = self.tableView.selectionModel().selectedIndexes()
        
        rows = sorted(index.row() for index in i)
        columns = sorted(index.column() for index in i)
        
        tempRow = set(rows)
        uniqueRows = list(tempRow)      
        
        tempCol = set(columns)
        uniqueCol = list(tempCol)      
        
        items = []
        for x in uniqueRows:
            entire = []
            for y in uniqueCol:
                ind = self.tableView.model().index(x, y)
                cell = str(self.tableView.model().data(ind))
                entire.append(cell)
            items.append(entire)
                    
        stream = io.StringIO()
        csv.writer(stream).writerows(items)
        QApplication.clipboard().setText(stream.getvalue())
               
    def copySheetNumber(self):
        selected = self.tableView.selectionModel().selectedIndexes()
        
        if selected:
            table = []
            for index in selected:
                if index.column() == 0:
                    table.append(index.data())
                    print(index.data())
            QApplication.clipboard().setText("\n".join(table))
            
    ###############################################################################################################
    def refresh(self):
        self.model.select()
        self.initNumResults = self.model.rowCount()
        self.numberResultsLabelMessage(self.model.rowCount())
    ###############################################################################################################


    ###############################################################################################################    
    def selectedRow(self):
        i = self.tableView.selectionModel().selectedRows()
        for row in sorted(i):
            x = row.row()
        return x
    
    resetSignal = QtCore.pyqtSignal()
    ###############################################################################################################

    ###############################################################################################################
    def clearSearch(self):
        self.sheetNumInputs.clear()
        query = "select * from {0}".format('table_1')
        self.model.setQuery(QSqlQuery(query))

        self.numberResultsLabelMessage(self.model.rowCount())
        
        self.resetSignal.emit()
    ###############################################################################################################


    ###############################################################################################################    
    def chartGenerator(self):
        ID = self.model.record(0).value('ID') #probably in need of a smarter decision in getting the ID
        #scatter_plotter(df,type_plot,section)
        #print(self.model.record(0).value('ID')) #record 0 gets the first record
        current_DB = table(self.database) #current database
        tables = current_DB.list_tables() #All the tables in the DB
      
        user_Frame = {}

        dataframe = sqlite3.connect(self.database + '.db')

        for tb in tables:
            temp = tb[0]
            print(temp)
            user_Frame[temp] = pd.read_sql_query("SELECT * FROM {0}".format(temp), dataframe)
            scatter_plotter(user_Frame[temp], "stud", temp,ID)
        
        #Just need to fix the chart generating stuff                    


    ###############################################################################################################

    ##Adding Data to Database

    def addDB_Table(self):
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                filetypes = (("Excel files","*.xlsx"),
                                                             ("all files","*.*")))


        value = root.filename
        temp = value.split("/")
        temp = temp[len(temp) - 1]
        
        dataframes = excel_read(value)#loaded in data values note is a dictionary
        Class_Add = table(self.database) #Getting the table information
        Class_Add.add_dataframe(dataframes)
        
        #self.database = temp
        #self.initDb(temp) #initializing Database and Model

        self.tableView.setModel(self.model) #for the table of the database to add in
        self.initNumResults = self.model.rowCount()
        self.numberResultsLabelMessage(self.model.rowCount())
        
        mainloop()
        



    ###############################################################################################################

    ###############################################################################################################
    ##Database Functionality
    def createDB(self):
        root= Tk()
        canvas1 = Canvas(root, width = 400, height = 300)
        canvas1.pack()
        entry1 = Entry (root) 
        canvas1.create_window(200, 140, window=entry1)

        def getSquareRoot ():  
            x1 = entry1.get()

            database(x1) # calling the database class
            
            self.database = x1 #The database to use
            
            label1 = Label(root, text = "Created Database is: " + x1)
            #label1 = tk.Label(root, text= float(x1)**0.5)
            canvas1.create_window(200, 230, window=label1)

            self.initDb(temp) #initializing Database and Model
            self.tableView.setModel(self.model) #for the table of the database to add in
            self.initNumResults = self.model.rowCount()
            self.numberResultsLabelMessage(self.model.rowCount())
            
        button1 = Button(text='Name of the Database: ', command=getSquareRoot)
        canvas1.create_window(200, 180, window=button1)

        root.mainloop()
        


    def openDB(self):
        
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                filetypes = (("Database files","*.db"),
                                                             ("all files","*.*")))


        value = root.filename
        temp = value.split("/")
        temp = temp[len(temp) - 1]
        self.database = temp
        self.initDb(temp) #initializing Database and Model

        self.tableView.setModel(self.model) #for the table of the database to add in
        self.initNumResults = self.model.rowCount()
        self.numberResultsLabelMessage(self.model.rowCount())
        
        mainloop()

    ###############################################################################################################
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QDesktopWidget().screenNumber(self)
        centerPoint = QtWidgets.QDesktopWidget().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database Analyzer"))
        self.groupBoxSearchPref.setTitle(_translate("MainWindow", "Search Preferences"))
        self.sheetNumLabel.setText(_translate("MainWindow", "Keywords:"))
        self.sheetNumSearchButton.setToolTip(_translate("MainWindow", "Search Based on Keywords"))
        self.sheetNumSearchButton.setText(_translate("MainWindow", "Search"))
        self.sheetNumLabel2.setText(_translate("MainWindow", "Document:"))
        self.sheetNumSearchButton2.setToolTip(_translate("MainWindow", "Search Based on Keywords"))
        self.sheetNumSearchButton2.setText(_translate("MainWindow", "Search"))
        self.groupBoxResults.setTitle(_translate("MainWindow", "Results"))
        
        self.Analysis.setToolTip(_translate("MainWindow", "For seeing charts corresponding to student result"))
        self.Analysis.setText(_translate("MainWindow", "Analyze"))
        self.resetSearch.setToolTip(_translate("MainWindow", "Clear Search"))
        self.resetSearch.setText(_translate("MainWindow", "Reset"))
        self.openSelected.setToolTip(_translate("MainWindow", "Open Selected Files"))
        self.openSelected.setText(_translate("MainWindow", "Choose Table"))
        
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Database.setTitle(_translate("MainWindow","&Database"))
        self.menu_Data.setTitle(_translate("MainWindow", "&Data"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        
        
        self.menuCopy_Selected.setTitle(_translate("MainWindow", "Copy Selected"))
        
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Filter.setText(_translate("MainWindow", "&ApplyFilter"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        
        self.actionCopy_Sheet_Number.setText(_translate("MainWindow", "Copy File Name"))
        self.actionCopy_Row.setText(_translate("MainWindow", "Copy Entire Row"))
        
        self.action_Refresh.setText(_translate("MainWindow", "&Refresh"))
        self.action_Search.setText(_translate("MainWindow", "&Search"))
        self.action_Help.setText(_translate("MainWindow", "Help"))

        
        #DATA
        self.action_createDatabase.setText(_translate("MainWindow", "Create Database"))
        self.action_openDatabase.setText(_translate("MainWindow", "Open Database"))
        self.action_addData.setText(_translate("MainWindow", "Add Data"))

import resources_rc

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    
    win = MainWindow()
    win.show()
    win.activateWindow()
    win.raise_()
    
    sys.exit(app.exec_())

