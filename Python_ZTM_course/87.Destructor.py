"""
# Destructors are called when an object gets destroyed. 
In Python, destructors are not needed as much as in C++ because Python has a garbage collector that handles memory management automatically. 

# The "__del__()" method is a known as a destructor method in Python. 
It is called when all references to the object have been deleted i.e when an object is garbage collected. 
"""

class test:
    def __init__(self): # Constructor
        print("Object Created")

    def __del__(self): # Destructor
        print("Object Deleted")

w = test()
del w # when we delete object that time "Destructor" will work.
print('\n')


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("My name is:", name)
        print("My age is:", age)
    def __del__(self):
        print("Destrutor Worked")

stud_1 = student("Gokulvasan", 23)
del stud_1

print('\n')

# Here i changed the order, Here construtor will work first, then destructor will work.
class student_2:
    def __del__(self): 
        print("Destrutor Worked")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("My name is:", name)
        print("My age is:", age)

stud_2 = student_2("GV", 24)
del stud_2

"""
If you want to know more,
https://www.geeksforgeeks.org/destructors-in-python/
"""