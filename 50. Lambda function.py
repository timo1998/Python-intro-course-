# functions that are written in one line 

# =============================================================================
# def double(x):
#     return x*2
# 
# print(double(5))
# =============================================================================

double = lambda x:x*2
multiply = lambda x,y:x*y

full_name = lambda first_name,last_name: first_name + " " + last_name

age_check = lambda age:True if age >= 18 else False

print(double(5))
print(multiply(2,3))

print(full_name('Timo','Roolant'))

print(age_check(18))