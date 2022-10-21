# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:35:51 2022

@author: Timor
"""

food = ["pizza","pineapple","Hamburgers","Hotdog"]

food[0] = "Sushi"
food.append("ice cream")
food.remove("Hotdog")
food.pop()
food.insert(0,"cake")
food.sort()


print(food[0])

for x in food:
    print(x)