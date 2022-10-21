from tkinter import * 

window = Tk()

def display():
    if((x.get())==1):
        print("You checked the button")
    else:
        print("You don`t agree")
        
x = IntVar()

check_button = Checkbutton(window,
                          text = "I agree to something",
                          variable = x,
                          onvalue = 1,
                          offvalue = 0,
                          command = display,
                          font=('Arial',20),
                          fg = 'Orange',
                          bg = 'black',
                          activeforeground  = "Orange",
                          activebackground = "black")

check_button.pack()

window.mainloop()