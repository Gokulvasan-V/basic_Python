"""
Types of Arguments

1) Position
2) Keywords
3) Default
4) Variable length
"""

# 1) Positional arguments

print("#1. This is from Positional parameter")
class studend_1:
     def __init__(self, name, age):
        self.name = name
        self.age = age
     def student_detials(self):
        print("My name is:", self.name)
        print("My age is:", self.age)

stud_1 = studend_1("GV",24)
stud_1.student_detials()
print('\n')

# 2) Keyword Arguments

print("#2. This is from Keyword parameter")
class studend_1:
     def __init__(self, name, age):
        self.name = name
        self.age = age
     def student_detials(self):
        print("My name is:", self.name)
        print("My age is:", self.age)

stud_1 = studend_1(age = 24, name = "GV")
stud_1.student_detials()
print('\n')

# 3) Default arguments

print("#3. This is from default parameter")
class studend_2:
     def __init__(self, name = 'GV', age = 24):
        self.name = name
        self.age = age
     def student_detials(self):
        print("My name is:", self.name)
        print("My age is:", self.age)

stud_2 = studend_2()
stud_2.student_detials()

print("----"*4)

stud_2_1 = studend_2("Gokul",23) # Over writting
stud_2_1.student_detials()
print('\n')

# 4) Variable length arguments

print("#4. This is from Variable length parameter")
class test:
    z = 0
    def __init__(self, x, *y):
        z = x
        for i in y:
            z+=i
            print(f"Sum of {z-i,i}:",z)

obj = test(10,20,30,40,50)

print("----"*4)

class test_2:
    z = 0
    def __init__(self, x, *y):
        z = x
        for i in y:
            z+=i
        print("Sum:",z)

obj = test_2(10,20,30,40,50)
