from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text= "Simple Calculator")
        self.lbl1.grid(row=0,column=0,columnspan=3,sticky=EW)

        self.lbl2 = Label(window, text = "Enter the 1st Number:")
        self.lbl2.grid(row=1,column=0)
        self.txt2 = Entry(window,bd=3)
        self.txt2.grid(row=1,column=1,sticky=W)
        self.lbl3 = Label(window,text="Enter the 2nd Number:")
        self.lbl3.grid(row=2,column=0)
        self.txt3 = Entry(window,bd=3)
        self.txt3.grid(row=2,column=1)


mywin = MyWindow(window)



window.mainloop()
