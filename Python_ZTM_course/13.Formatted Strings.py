
name = 'Gokulvasan'
age = 23

print('hii ' + name + '. You are ' + str(age)
      + ' Years old.')

'''
instead of this we can use
'''
# Formatted string

print(f'Hii {name}. You are {age} Years old.')

print('hiii {}. you are {} years old'.format('Gokulvasan',23))

print('Hiii {}. you are {} years old'.format(name,age))

# Here we denote with the value 0 --> name, 1 --> age.
print('Hiii {0}. you are {1} years old'.format(name,age))

print('Hiii {s_name}. you are {s_age} years old'.format(s_name= "GV",s_age=24))
#print(s_name, s_age) # it will show error because it's local variables.

# printed with space
print('\nHiii {}.\nyou are {} years old'.format(name,age))