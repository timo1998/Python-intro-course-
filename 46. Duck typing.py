# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:02:52 2022

@author: Timor
"""

class Duck:
    
    def walk(self):
        print("This duck is walking")
        
    def talk(self):
        print("This duck is qwuacking")
        
class Chicken:

    def talk(self):
        print("This chicken is clucking")
        
class Person():
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)