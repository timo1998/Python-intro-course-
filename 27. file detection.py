# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:35:34 2022

@author: Timor
"""

import os 

path = 'C:\\Users\\Timor\\OneDrive\\Python\\Course\\Test.txt'

if os.path.exists(path):
    print("This location exists")
    if os.path.isfile(path):
        print("Dit is een bestand")
    else:
        print("Dit is geen bestand")
else:
    print("This location does not exists")