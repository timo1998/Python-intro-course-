# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:32:25 2022

@author: Timor
"""

#De oude manier om classen te definieëren:
    

# =============================================================================
# class Rectangle:
#     pass
# 
# class Square(Rectangle):
#     
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         
# class Cube(Rectangle):
#     
#     def __init__(self, length, width, height):
#         self.length = length
#         self.width = width
#         self.height = height 
# =============================================================================
        
#Maar we schrijven een stukje code liever 1 keer en gebruiken dit vaker. De code hierboven wordt dan:
        
class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def Area(self):
        return self.length*self.width
    
        
class Cube(Rectangle):
    
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height 
        
    def Volume(self):
        return self.length*self.width*self.height
        
square = Square(3,3)
cube = Cube(3,3,3)

print(cube.Volume())
print(square.Area())
