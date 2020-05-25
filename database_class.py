import sqlite3

class database:
    #Functionalities to include in the database
    #Adding opening the database which is from the initialization needs the database path
    #init
    #Next step is to add the pickly file to the database which would be create_table functionality
    #create table
    
    def __init__(self,db_name):
        db_name = db_name + ".db"
        self._dbname = db_name
        self._dba = sqlite3.connect(db_name)
        self._saving = self._dba.cursor()

    def database_name(self):
        return self._dbname
