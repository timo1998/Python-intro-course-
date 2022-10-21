# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:45:35 2022

@author: Timor
"""

student = ("Bro",8,"male")

print(student.count("Bro"))
print(student.index("male"))

for x in student :
    print(x)
    
    
if "Bro" in student:
    print("Bro is here")    