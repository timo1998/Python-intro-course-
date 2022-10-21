# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:06:09 2022

@author: Timor
"""

# kwargs = parameter that will pack all arguments into a dictionary 
# usefull so that a function can accept a varying amount of keyword arguments 

def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(first ="Bro",middel = "Dude", last = "Code")