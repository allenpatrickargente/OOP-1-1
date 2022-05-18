from tkinter import*

window = Tk()
window.title("simple calculator")
window.geometry("400x200+20+10")

class Mywindow:
    def __init__(self,window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.place(relx=0.50, y=50, anchor="center")
        self.lbl2 = Label(window, text = "Input 1st Number")
        self.lbl2.place(x=50, y=80)
        self.txt2 = Entry(window, bd=3)
        self.txt2.place(x=180, y=80)
        self.lbl3 = Label(window, text="Input 2nd Number")
        self.lbl3.place(x=50, y=120)
        self.txt3 = Entry(window, bd=3)
        self.txt3.place(x=180, y=120)

        self.btn1 = Button(window, text="Addition",command=self.add)
        self.btn1.place(x=50, y=150)
        self.btn1.bind('<Button-1>',self.add)

        self.btn2 = Button(window, text = "Subtaction")
        self.btn2.place(x=120, y=150)
        self.btn3 = Button(window, text = "MUltiplication")
        self.btn3.place(x=200, y=150)
        self.btn4 = Button(window, text = "Division")
        self.btn4.place(x=300, y=150)

        self.lbl4 = Label(window, text = "Result")
        self.lbl4.place(x=50,y=200)
        self.txt4 = Entry(window , bd=3)
        self.txt4.place(x=120, y=200)


    def add(self):
        self.txt4.delete('0',END)
        num1=int(self,txt2,get())
        num2=int(self.txt3.get())
        answer = num1+num2
        self.txt4.Insert(END,str(answer))



mywin = Mywindow(window)



window.mainloop()