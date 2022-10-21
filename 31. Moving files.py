# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:48:52 2022

@author: Timor
"""

import os

source = 'C:\\Users\\Timor\\OneDrive\\Python\\Course\\Test.txt  '
Destination = 'C:\\Users\\Timor\\OneDrive\\Documenten\\Bureaublad\\Test.txt' 

try:
    if os.path.exists(Destination):
        print("File allready is there")
    else:
        os.replace(source,Destination)
        print("Source is moved" )

except FileNotFoundError:
    print("Source was not found")