"""
Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘+’ operator is overloaded by int class and str class. 
You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, 
this is called Operator Overloading.
"""

# normal addiction method
a = 10
b = 20
print(a + b)

# actually, what python does in the addiction operation...?
a = 30
b = 40
print(int.__add__(a,b))

# string concadination
a = "happy"
b = "learning"
print(str.__add__(a,b))

# we will give other types

# a = "happy"
# b = 20
# print(str.__add__(a,b)) # ERROR

#-------------------#-------------------#-------------------#-------------------#

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

s1 = Student(30,40)
s2 = Student(50,40)
# s3 = s1 + s2 # ERROR --> unsupported operand type(s) for +: 'Student' and 'Student'
print('\n')
#-------------------#-------------------#-------------------#-------------------#

# HERE, we overwrite (or) modify the the default addition concept.

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,temp): # HERE, we modify the '__add__' method.
        first_stud = self.m1 + self.m2 # self --> 1st object (s1)
        second_stud = temp.m1 + temp.m2 # temp --> 2nd object (s2)
        total = Student(first_stud , second_stud)
        return total

s1 = Student(30,20)
s2 = Student(80,20)
total = s1 + s2

print(total.m1)
print(total.m2)
# print(total)