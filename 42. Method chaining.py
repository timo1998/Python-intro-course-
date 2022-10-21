# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:24:32 2022

@author: Timor
"""

class Car:
    
    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
        
    def brake(self):
        print("You step on the brakes")
        return self
    
        
    def turn_off(self):
        print("You turn off the engine")
        return self
    
        
car = Car()

car.turn_on()
car.drive()

#Or :
    
car.turn_on().drive().brake().turn_off()

#Of voor meer overzicht:
    
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off
