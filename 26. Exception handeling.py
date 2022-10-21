# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:12:26 2022

@author: Timor
"""

# ecception is an event detect during an execution that interrupted the flow 
# of a program 

try:
    numerator = int(input("Enter a number to divide :"))
    denominator = int(input("Enter a number to be divided :"))
    result = numerator / denominator  
except ZeroDivisionError: 
    print("You can't divide by zero")  
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Enter only numbers please ")
except Exception:
    print("Oops, something whent wrong")
else: #Alleen uitvoeren als er geen exceptions zijn 
    print(result)
finally: 
    print("This will always execute")
#Je kunt met except speciale exceptions opvangen, door bijvoorbeeld zerodivisionerror
#er achter te typen, maar je kunt ook alle errors opvangen door except exception. 

