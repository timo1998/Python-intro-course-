# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:43:14 2022

@author: Timor
"""

# Abstract classes prevent a user from creating an object of that class
# It`s more lika a template o an class
# Stel je voor dat je een game ontwerp en dat de gebruiker een auto of een motor 
# mag ontwerpen. De gebruiker mag dan geen toegang hebben tot de vehicle class

# =============================================================================
# De volgende class willen we omzetten naar een abstract class:
# class Vehicle:
#     
#     def go(self):
#         pass
# =============================================================================

# Elke class die inherit van de abstract class moet in dit geval de go method 
# Overschrijven. Anders zal python de code niet runnen. 
    
from abc import ABC, abstractmethod #ABC staat voor abstract class 

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    
    def go(self):
        print("You drive the car")
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
    
