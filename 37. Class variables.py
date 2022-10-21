# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:33:40 2022

@author: Timor
"""

#Het verschil tussen class variables en Instance variables. Instance variables 
#kunnen worden gekozen, zoals kleur, model en merk. Maar alle auto`s zullen 
#vier wielen hebben. Dit noemen we een class variable.

class Car :
    
    wheels = 4 #Class variabless 
            
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model 
        self.year = year 
        self.color = color
 
# =============================================================================
# car_1 = Car("Ford","Mustang",1998,"Red")
# car_2 = Car("Ford","Mustang",1998,"Red")  
#  
#     
# car_1.wheels = 2 
#  
# print(car_1.wheels)
# print(car_2.wheels)
# =============================================================================

Car.wheels = 2 #Nu hebben we overal het aantal wielen aagepast. 

print(Car.wheels)