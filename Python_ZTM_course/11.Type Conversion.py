print(str(100))

# print(type(str(100))) 


a = str (1000)
b = int (a)

print(type('a is',a))
print(type('b is',b))

"""
We're converting the type of our data types
"""

birth_year = input('what year were you born? ')
age = 2019 - birth_year
# age = 2019 - int(birth_year)

print(f'your age {age}')