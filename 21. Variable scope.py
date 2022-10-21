# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:46:41 2022

@author: Timor
"""

name = "Bro" #global variable (overal aanroepbaar)

def display_name():
    name = "code" #local variable (alleen lokaal in bijvoorbeeld een funnctie beschikbaar)
    print(name)
    
display_name()
print(name )
#Je kunt meerdere soorten variabelen gebruiken. Python heeft hier vooranngs regels
#voor. Namelijk LEGB (Local, Enclosing, Global, Built-In)    