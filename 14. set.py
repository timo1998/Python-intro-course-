# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:48:46 2022

@author: Timor
"""

utensils = {"fork","spoon","knive"}
dishes = {"bowl","plate","cup","knive"}

utensils.update(dishes)

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))

print(utensils.intersection(dishes))

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

for x in utensils:
    print(x)