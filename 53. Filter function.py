# Filter function : creates a collection of elements from an iterable for which a function retruns true 

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

#We willen een lijst van iedereen die ouder dan 18 is. 

age = lambda data:data[1] >= 18

drinking_budies = list(filter(age,friends))

for i in drinking_budies:
    print(i)