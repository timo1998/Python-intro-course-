# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:08:25 2022

@author: Timor
"""

import random 

x = random.randint(1, 6)
y = random.random()
mylist = ['Rock','Paper','Scissors']

z = random.choice(mylist)

print(z)
print(y)
print(x)

cards = [1,2,3,4,5,6,7,8,9,10,'j','q','k','a']
random.shuffle(cards)

print(cards)