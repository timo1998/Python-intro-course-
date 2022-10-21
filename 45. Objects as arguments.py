# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:57:11 2022

@author: Timor
"""

class Car:
    
    color = None
    
class Motorcycle:
    
    color = None
    
def change_color(vehicle,color):
    
    vehicle.color = color 
    
car_1 = Car()
car_2 = Car()
car_3 = Car()
motorcycle = Motorcycle()

change_color(car_1,"Red")
change_color(car_2,"White")
change_color(car_3,"Blue")
change_color(motorcycle,"Black")

print(car_1.color)
print(motorcycle.color)