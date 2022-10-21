# Walrus operator :=

# assigns values to variable as part of a larger expression

happy = True 
print(happy)

#of op de volgende manier:
    
print(happy := True)

# =============================================================================
# foods = list()
# while True :
#     food = input("What food do you like?")
#     if food == "quit":
#         break 
#     foods.append(food)
# =============================================================================
    
#Of het hele programma korter geschreven als volgt:
    
foods = list()
while food := input("What food do you like? ") != "quit":
    foods.append(food)

