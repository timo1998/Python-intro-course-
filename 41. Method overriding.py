# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:21:11 2022

@author: Timor
"""

class Animal:
    
    def eat(self):
        print("This animal is eating")
        

class Rabbit(Animal):
    
    def eat(self):
        print("This animal is eating a carrot")
        
        
rabbit = Rabbit()

rabbit.eat()


    