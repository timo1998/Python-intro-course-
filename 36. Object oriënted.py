# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:52:59 2022

@author: Timor
"""

class Car :
    
    #De object is in dit geval (self)
    #Hieronder staat de zogenaamde constructor, bij het invullen wordt self 
    #automatisch door python ingevuld, self refereert in dit geval naar car_1 
    #Dit hier onder omschrijft waat een object heeft 
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model 
        self.year = year 
        self.color = color
     
    #Hieronder staan zogenaamde methods
    def drive(self):
        print("This " + self.model + " is driving")
    
    def stop(self):
        print("This car is stopping")

car_1 = Car("Chevy","Corvet",2021,"Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()