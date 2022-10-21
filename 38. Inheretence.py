# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:58:38 2022

@author: Timor
"""

# Met behulp van inheretence kan een nieuwe class informatie overnemen uit 
# een andere class. 'Vaak wordt er gesproken van een parent child class, child classes 
# nemen dan alles over van de parent class. Het grote voordeel is dat als er een weiziging 
# wordt gemaakt in de animal class deze wijziging ook in alle inheritance classen zit. 

class Animal:
    
    alive = True 
    
    def eat(self):
        print("Thsi animal is eating")
        
    def sleep(self):
        print("This animal is sleeping")
        
class Rabit(Animal):
    
    def run(self):
        print("This rabit is running")

class Fish(Animal):
    
    def swim(self):
        print("Thisfish is swimming") 

class Hogh(Animal):
    
    def run(self):
        print("This hogh is flying")

rabit = Rabit()
fish = Fish()
hogh = Hogh()

rabit.eat()
rabit.run()