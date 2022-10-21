# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 20:10:57 2022

@author: Timor
"""

name = "Timo Roolant"

# Indexing:
#variable["startindex","stopindex + 1","step"]
# Korter schrijven :
# beginnen bij 0 : variable[:"stopindex"]
# stoppen bij end : ["Begin":]

voornaam = name[0:4:1]
achternaam = name[5::1]

print(voornaam)
reversed_name = name[::-1]

print(reversed_name)

# slice function :

webpage = "http://google.com"

# definieer een slice, een soort masker dat je kunt toepassen op verschillende objecten 


slice = slice(7,-4,1)

print(webpage[slice])