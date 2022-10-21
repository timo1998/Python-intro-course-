# zip function = aggregates elements from two or more iterables creates a zip object\
# with paired elements for each element. 

usernames = ["Dude","Bro","Mister"]
passwords = ("p@sword","abc123","guest")

users = list(zip(usernames,passwords))


for i in users :
    print(i)
