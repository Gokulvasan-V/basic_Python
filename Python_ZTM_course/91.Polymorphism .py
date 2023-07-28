"""
The word polymorphism means having many forms. 
In programming, polymorphism means the same function name (but different signatures) being used for different types. 
The key difference is the data types and number of arguments used in function.
"""

"""
Poly - means 'many'
Morphism - means 'Forms'
"""

# Examples:

# 1) using '+' operator

num_1 = 10
num_2 = 20
print(num_1 + num_2)

str_1 = "Happy"
str_2 = "Learning"
print(str_1 + str_2)
print('\n')

#-------------------#-------------------#-------------------#-------------------#

"""
Here, we use '+' operator for both program, But our output is different.
Here, '+' operator performs different different forms.
"""
# 2) using 'len' function

print(len("Happy Learning"))

print(len(["hello", "hii", "different"]))

print(len({"Name":"gokul", "Age":24}))

"""
Here also we use 'len' function but we get different different outputs
"""


"""
These are the few examples of 'Polymorphism'
"""

#-------------------#-------------------#-------------------#-------------------#

"""
Types of Polymorphism

1) Method Overloading
2) Method Overridding
3) Operator Overloading
"""