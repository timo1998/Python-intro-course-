# Map function : applies a function to ech item in an iterable (list, tuple etc)


store = [("Shirt",20.00),
         ("Pants",25.00),
         ("Jacket",50.00),
         ("Socks",10.00)]

#Dollers veranderand naar euros 

to_euros = lambda data: (data[0],data[1]*0.82)
to_dolars = lambda data: (data[0],data[1]/0.82)

store_dolars = map(to_dolars,store)

for i in store_dolars :
    print(i)
    
