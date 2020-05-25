# to open files in the listbox
#https://pythonprogramming.altervista.org/tkinter-show-the-files-in-the-folder-in-a-listbox/ 
 
##import tkinter as tk
##import os
##from win32com.client import Dispatch
##import tkinter.filedialog



##def reading_from_directory(): #audio and reading info in file
##    s = Dispatch("SAPI.SpVoice")
##     
##    # WINDOW CREATION
##    win = tk.Tk()
##    geo = win.geometry
##    geo("400x400+400+400")
##    win['bg'] = 'orange'
##     
##    # get the list of files
##    flist = os.listdir()
##     
##    lbox = tk.Listbox(win)
##    lbox.pack()
##     
##    # THE ITEMS INSERTED WITH A LOOP
##    for item in flist:
##        lbox.insert(tk.END, item)
##     
##     
##    def showcontent(event, audio=0):
##        x = lbox.curselection()[0]
##        file = lbox.get(x)
##        with open(file, 'r', encoding='utf-8') as file:
##            file = file.read()
##        text.delete('1.0', tk.END)
##        text.insert(tk.END, file)
##     
##     
##    def audio():
##        s.Speak(text.get('1.0', tk.INSERT))
##     
##     
##    def opensystem(event):
##        x = lbox.curselection()[0]
##        os.system(lbox.get(x))
##     
##     
##    button = tk.Button(win, text="audio")
##    button['command'] = audio
##    button.pack()
##     
##    text = tk.Text(win, bg='cyan')
##    text.pack()
##    # BINDING OF LISTBOX lbox
##    lbox.bind("<<ListboxSelect>>", showcontent)
##    lbox.bind("<Double-Button-1>", opensystem)
##    # BUTTON
##     
##    win.mainloop()

from tkinter import *
from tkinter import filedialog

def directory_viewer():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                filetypes = (("Database files","*.db"),
                                                             ("all files","*.*")))
    #print (root.filename)
    mainloop()
    value = root.filename
    temp = value.split("/")
    temp = temp[len(temp) - 1]
    #return value


    
