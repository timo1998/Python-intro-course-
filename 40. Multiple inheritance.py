# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:15:18 2022

@author: Timor
"""

class Prey:
    
    def flee(self):
        print("This animal flees")

class Predator:
    
    def hunt(self):
        print("This animal is hunting")
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
