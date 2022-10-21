

def submit():
    
    food = []
    
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
        
    for index in food:
        print(index)
 
 
    
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height = listbox.size())

def delete():
    
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    
    
    listbox.config(height = listbox.size())
    
from tkinter import * 

window = Tk()

listbox = Listbox(window,
                  bg = "yellow",
                  font = ("Constantia",35),
                  width = 12,
                  selectmode = MULTIPLE
                  )

listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Pudding")
listbox.insert(4,"Salad")
listbox.insert(5,"Fries")




entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,
                text = "add",
                command = add)

addButton.pack()


button = Button(window,
                text = "Submit",
                command = submit)

button.pack()

deleteButton = Button(window,
                      text = "Delete",
                      command = delete)

deleteButton.pack()

listbox.config(height = listbox.size())

window.mainloop()