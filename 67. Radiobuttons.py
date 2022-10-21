from tkinter import * 

food  = ["Pizza","hamburger","hotdog"]


window = Tk()



x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text = food[index],
                              variable = x,
                              value = index,
                              padx = 25,
                              font = ("Impact",50),
                              indicatoron = 0, # elemenate circle indicators
                              width = 375,
                              )
    radiobutton.pack(anchor = W)




window.mainloop()