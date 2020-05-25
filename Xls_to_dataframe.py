import pandas as pd
import string
import re
import Stats_analysis
from Stats_analysis import *


def data_sections(data,cols):
    sections = {}
    id_col = cols[0] #Getting the main identifier column

    knowledge = cols.index('Knowledge')
    communication = cols.index('Communication') #First
    thinking = cols.index('Thinking') #Second
    application = cols.index('Application') #Third
    distribution = cols.index('Distribution') #FIndig the end for the table

    #print(knowledge,communication,thinking,application,distribution)
    #print(cols[knowledge:communication]) 
    sections['Knowledge'] = data[[id_col] + cols[knowledge:communication]]
    sections['Communication'] = data[[id_col] + cols[communication:thinking]]
    sections['Thinking'] = data[[id_col] + cols[thinking:application]]
    sections['Application'] = data[[id_col] + cols[application:distribution]]


    ##This was the older name of changing the columns 
    for section in sections:
        sections[section].to_csv('export_dataframe.csv', index = False, header=False)
        sections[section] = pd.read_csv('export_dataframe.csv')
    return sections
    

    
        
    

def excel_read(path): #This will be changing
    #ID,db,table
    #xls_file_path = input("Please input the file path of your excel file: ")
    xls_file_path = path
    
    #xls_file_path = xls_file_path.replace('\\','/')
    #if (xls_file_path[0] == '"'):
    #    xls_file_path = xls_file_path[1:-1]
    print(xls_file_path)
    dataframe = pd.read_excel(xls_file_path)
 
    sample = dataframe.columns
    columns = []
    
    for column in sample:
        columns.append(column)
    #print(columns)
        
    dataframes = data_sections(dataframe,columns)  #Note this a dictionary of datafames with each heading
    #print(dataframes['Communication'].columns)
    #print(dataframes['Communication'].values)
    print(dataframes['Communication'])

    #comm = dataframes['Communication'] #remember to turn off
    #columns = dataframes['Communication'].columns
    #values = dataframes['Communication'].values
    #print(values[0][1:len(values)]) #values for each

  
    #scatter_plotter(comm,"stud","Communication") #remember to turn off 
    #scatter_plotter(values[0][1:len(values)], values[1][1:len(values)],"stud","Knowledge",values[1][])
    #next is to focus on the student analysis


    
    return dataframes

#excel_read("C:/Users/Gio.Harvey/Documents/Mommy/Final_Marks_Modified.xlsx")  



