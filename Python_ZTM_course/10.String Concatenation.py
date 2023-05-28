# Concatenating --> it simply means adding strings together.

str1="Hello"
str2="World"

print ("String 1:",str1)
print ("String 2:",str2)

str=str1+str2 # if we print this, there is no space

str_s=str1+' '+str2 # if we print this, we can make space

print("Concatenated two different strings:",str)
print("Concatenated two different strings with space:",str_s)

# string concatenation only works with strings.
# we can't do

print('hello'+5) # it will show error

# (or) we can do below one (or) we can do Type Conversion

print('hello'+'5') 