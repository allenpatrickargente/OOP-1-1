from tkinter import *
window = Tk()

window.geometry("550x280+30+20")
window.title("Midterm in OOP")

fn = Label(window, text="Enter your Fullname", fg="Red")
fn.place(x=50, y=100)
fnbox = Entry(window, bd = 4, font = ("verdana",20))
fnbox.place(x=250, y=100)
txtfld = Entry(window, bd = 4, font = ("verdana",20))
txtfld.place(x=250, y=200)

def Display():
    dfn = Label(window, text=fnbox.get(), bd=4, font = ("verdana", 13))
    dfn.place(x=260, y=205)

displayButton = Button(window, text="Click to display your fullname", padx=4, pady=3, command=Display, fg="red")
displayButton.place(x=50, y=210)

window.mainloop()