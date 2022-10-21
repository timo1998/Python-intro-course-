# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:12:24 2022

@author: Timor
"""

# str.format() = optional method that gives users more control when desplaying
# output

animal = "cow"
item = "moon"

#print("The " + animal + " jumped over the "+item)

#print("The {} jumped over the {}".format(animal,item))
#print("The {1} jumped over the {0}".format(animal,item)) # Positional arguments 

#print("The {animal} jumped over the {item}".format(animal="cow",item="Moon")) # Positional arguments

text = "The {} jumped over the {}"

# Met behulp van {:10} kun je aangeven hoeveel plaatsen er gereserveerd moeten
# worden voor je argument. je kunt ook aangeven waar je argument alligned moet worden
# {:<10} left aligning 
# {:>10} right aligning 
# {:^10} center alligned
# {'variable':<10} variabele declaren voor de align statement 

print("The {:10} jumped over the {:10}".format(animal,item)) # Positional arguments

print(text.format(animal,item))

# Bepalen hoeveel comma getallen weergegeven moeten worden 
pi = 3.14159

print("The number pi is {:.2f}".format(pi))
# Of binair 
print("The number pi is {:b}".format(1000))
print("The number pi is {:o}".format(1000))
print("The number pi is {:X}".format(1000))
print("The number pi is {:E}".format(1000))






 