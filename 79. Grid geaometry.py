from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter yout info").grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20).grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ").grid(row=2,column=0)
lasttNameEntry = Entry(window).grid(row=2,column=1)

EmailLabel = Label(window,text="Email: ").grid(row=3,column=0)
EmailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row = 4,column=0,columnspan=2)




window.mainloop()