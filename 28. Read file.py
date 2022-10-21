# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:42:14 2022

@author: Timor
"""

with open('C:\\Users\\Timor\\OneDrive\\Python\\Course\\Test.txt') as file:
    print(file.read())
    
print(file.closed) 

#Het is beter om exceptions te gebruiken 
 
try:  
    with open('C:\\Users\\Timor\\OneDrive\\Python\\Course\\Tes.txt') as file:
        print(file.read())
except FileNotFoundError:   
    print("That file was not found") 