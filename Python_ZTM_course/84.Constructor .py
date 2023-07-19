"""
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.
"""

"""
Types of constructors : 

1) default constructor --> The default constructor is a simple constructor which doesn't accept any arguments
2) parameterized constructor --> constructor with parameters is known as parameterized constructor. 
"""

# 1) default constructor

class test_1:
    def __init__(self): # constructor
        print("Hai")
    
    def hello(self):
        print("hello")

test = test_1() # here we didn't mention any method. Print statement work automatically without method calling.

test.hello() # here we want to mention method name. Otherwise it won't run.
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

class student:
    def __init__(self):
        name = "Gokulvasan V"
        age = 24
        print("My name is:", name)
        print("My age is:", age)

stud = student()
stud_2 = student()
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

class person:
    def __init__(self):
        print("1")
    
    def __init__(self):
        print("2")

person = person()  # we can't give '__init__' two times. it will overwrite the method.

"""
Want to know more,
https://www.geeksforgeeks.org/constructors-in-python/
"""