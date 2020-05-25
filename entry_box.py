from tkinter import *  
  
##top = Tk()  
##  
##top.geometry("400x250")
##
##value = StringVar()
##  
##name = Label(top, text = "Name").place(x = 30,y = 50)  
##  
##email = Label(top, text = "Email").place(x = 30, y = 90)  
##  
##password = Label(top, text = "Password").place(x = 30, y = 130)  
##  
##sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)  
##  
##
##e1 = Entry(top).place(x = 80, y = 50)  
##  
##  
##e2 = Entry(top,textvariable = ).place(x = 80, y = 90)  
##  
##  
##e3 = Entry(top).place(x = 95, y = 130)
##
##value = e1.get()
##print(value)
##  
##top.mainloop()  



from tkinter import *

def createElement():

    root= Tk()
    canvas1 = Canvas(root, width = 400, height = 300)
    canvas1.pack()
    entry1 = Entry (root) 
    canvas1.create_window(200, 140, window=entry1)

        def getSquareRoot ():  
            x1 = entry1.get()
            label1 = Label(root, text = x1)
            #label1 = tk.Label(root, text= float(x1)**0.5)
            canvas1.create_window(200, 230, window=label1)
            
    button1 = Button(text='Name of the Database', command=getSquareRoot)
    canvas1.create_window(200, 180, window=button1)

    root.mainloop()

