# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:11:35 2022

@author: Timor
"""

class Organism:
    
    alive = True 
    
class Animal(Organism):
    
    def eat(self):
        print("This animal eats")
        
class Dog(Animal):
    
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.bark()
    