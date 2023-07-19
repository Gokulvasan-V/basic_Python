# Parameterized Constructor --> Constructor with parameters is known as parameterized constructor. 

class student:
    def __init__(self, name, age): # here we passed parameter, that's why it is called Parameterized Constructor.
        print("My name is:", name)
        print("My age is:", age)

stud_1 = student("Gokulvasan", 23)
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

class student_2:
    def __init__(self, name):
        age = 23
        print("My name is:", name)
        print("My age is:", age)

stud_2 = student_2("Gokulvasan V")
print('\n')

#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#

# this is the best method. we can use parameter which O/P we want.
class studend_3:
     def __init__(self, name, age):
        self.name = name
        self.age = age
     def student_detials(self):
        print("My name is:", self.name)
        print("My age is:", self.age)

stud_3 = studend_3("GV",24)
stud_3.student_detials()
print("-----"*3)

stud_3_1 = studend_3("VGV",23)
stud_3_1.student_detials()
print('\n')


#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#--------#
