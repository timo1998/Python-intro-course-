# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:55:31 2022

@author: Timor
"""

capitals = {'Usa':'Washington DC','The Netherlands':'Amsterdam','China':'Beijing','Russia':'Moskou'}

capitals.update({'Germany':'Berlin'})
capitals

#print(capitals['Russia'])
capitals.get('Germany')
capitals.pop('Russia')

print(capitals.keys())

print(capitals.items())
print(capitals.values())

for key,value in capitals.items():
    print(key.value)