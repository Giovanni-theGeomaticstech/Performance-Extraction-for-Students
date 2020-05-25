#!/usr/bin/env python
# coding: utf-8

# In[2]:


###########################################################################################################################


import database_class
from database_class import *
import Xls_to_dataframe
from Xls_to_dataframe import excel_read
import numpy as np
import pandas as pd
import string
import matplotlib.pyplot as plt 
from scipy import stats
from numpy import mean, absolute,median
from pandas import DataFrame
import pickle
import sqlite3
import string
import re




# Thinking is that in the building is have a field added which is the markers reference marks.
#     Have a unique ID name John DOe and the type of grade


    

class table():

    def __init__(self,db_name):
        table_name = ""#input("Give a table_name: ")
        self._database = database(db_name)
        self._tbname = table_name
        
    def create_table(self,code):
        print(self._database)
        self._code = code
        print(self._database.database_name())
        self._database._saving.execute("CREATE TABLE if not exists {0} ({1} TEXT)".format(self._tbname,code))#'CSA'
        self._database._dba.commit()
    
    #Adding a dataframe to the table
    def add_dataframe(self,dataframes):

        for df in dataframes:
            dataframes[df].to_sql(df,self._database._dba, if_exists='replace', index = False)
    
    def delete_table(self,table_name):
        self._database._saving.execute('DROP table if exists {0}'.format(table_name))
    
    def add_column_to_table(self,column_name):
        column_info = "Alter table {0} Add Column {1} TEXT".format(self._tbname,column_name)
        self._database._saving.execute(column_info)
        self._database._dba.commit()
        
        #for column_name in columns:
         #   self._saving.execute("Alter table {0} Add Column {1} TEXT".format(table_name,column_name))
          #  self._database.commit()
    
    #This is for inserting a new field into a table
    def insert_into_Table(self,column,value):
        table_insert = "INSERT INTO {0}({1}) VALUES({2})".format(self._tbname,column,value)
        self._database._saving.execute()
        self._database.commit()
    
    #This is for updating a field in the table
    def update_Table(self,column_change_value,value,id_column):
        update_table = "UPDATE {0} SET {1} = {2} where {3} = {4}".format(self._tbname,column,column_change_value,id_column)
        self._database._saving.execute()
        self._database._dba.commit()
    
    #This is for fetching info from a table
    def fetch_info(self):
        fetched_info = "Select * From {0}".format(self._tbname)
        self._database._saving.execute()
        rows = self._saving.fetchall()
        for row in rows:
            print(row)
    
    #Listing all the tables in a table using the master table
    def list_tables(self):
        table_list = self._database._saving.execute('SELECT name from sqlite_master where type= "table"')
        return table_list.fetchall()
        #print(table_list.fetchall())
    
    def virtual_execute(self):
        table_select = '''Select * FROM {0}'''.format(self._tbname) #Dynamic setting
        self._database._saving.executescript(table_select)
        self._database._dba.commit()
        
        self._saving.executescript('''create VIRTUAL TABLE search_articles USING FTS5(Art_Number,Art_Name,FullText) ;''') #Virtual table runs directly
        self._database._dba.commit()
        
        edited_query = '''insert into search_articles select Number, Name, Content from {0};'''.format(self._tbname)
        self._database._saving.executescript(edited_query) #
        self._database._dba.commit()
        
    def execute_query(self,search): #not query list is a list of strings of the query
        temp = search.split(' ') #Just in case if there a multiple words
        word_1 = temp[0] + '* '
        word_2 = temp[1] + '*' #Recheck just in case
        combined_word = word_1 + word_2
        matching_query = '''select Art_Number, Art_Name, Content, Page, Commentary FROM search_articles
                        JOIN {0} ON search_articles.Art_Number = {0}.Number
                        WHERE search_articles MATCH '{1}' Order by bm25(search_articles,0,20,10); '''.format(self._tbname,combined_word)

        self._database._saving.executescript(matching_query)
        self._database._dba.commit()

    def sql_to_dataframe(self):
        #dataframe = pd.read_sql_table(self._tbname,self._database)
        dataframe = pd.read_sql(self._tbname,self._database._dba)
        print(dataframe)
        #return dataframe
    
        
        
#No GUI Testing 
##def database_func(dbname,code_type,dataframe):
##    columns = list(dataframe.columns.values)
##    data = dataframe
##    sample_db = table(dbname,code_type)
##    sample_db.create_table(code)#columns
##    sample_db.add_dataframe(data) #adding the db data to the file
##    sample_db.list_tables()
##    
##   
###Receiving the data
##
##while (True): #Building the user system
##    database_name = input("Please enter the database name: ")
##    code = input("Please enter the grade section: ") #fix that part of the name of file name
##    dataframe = excel_read()
##    database_func(database_name,code,dataframe)
##    user_input = input("Do you want to keep going n for no:")
##    if(user_input == "n"):
##        break






