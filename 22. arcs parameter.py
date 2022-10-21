# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:51:07 2022

@author: Timor
"""

# args = a parameter that will pack all arguments into a tuple'
# Usefull so that a function can accept a varying amount of arguments

def sum(num1,num2):
    sum1 = num1 + num2
    return sum1

print(sum(1,2))

def add(*args):
    som = 0
    for i in args:
        som += i 
    return som

print(add(1,2,3))