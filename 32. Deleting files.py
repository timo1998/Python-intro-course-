# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:53:13 2022

@author: Timor
"""

import os
import shutil

source = 'C:\\Users\\Timor\\OneDrive\\Python\\Course\\copy_Test.txt  '


try: 
    os.remove(source)
    
except FileNotFoundError:
    print("File not found")

# Now we are going to remove directories 

path = 'C:\\Users\\Timor\\OneDrive\\Python\\Course\\test'

# For removing folders that contain files you have to use the shutil library, be 
# extremely carefull when doing this since this will remove everything in that folder. 



try:
    shutil.rmtree(path)
except FileNotFoundError:
    print("Your file is not found")
except PermissionError:
    print("Ypu can not delete that wit this function")