# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:59:25 2022

@author: Timor
"""

rows = int(input("How many rows: "))
colums = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="")
    print()