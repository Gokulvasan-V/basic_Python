"""
here we will perform without methods.
"""

class person:
    name = ""
    age = 0
    gender = ""

person_1 = person()
person_1.name = "Gokulvasan V"
person_1.age = 23
person_1.gender = "Male"

person_2 = person()
person_2.name = "GV"
person_2.age = "24"
person_2.gender = "Male"

print("person_1 name is: ", person_1.name)
print("person_1 age is: ", person_1.age)
print("person_1 gender is: ", person_1.gender)

print('\n')

print("Person_2 name is: ", person_2.name)
print("Person_2 age is: ", person_2.age)
print("Person_2 gender is: ", person_2.gender)
print('\n')

# here I'm using without 'self' parameter.
class person_1:
    name = ""
    age = 0
    gender = ""
    def print_detials(self): # here we must give 'self' parameter, 'self' simply reffers to object name.
        print("My Name is: ", c.name) # but here i didn't use 'self.name'
        print("My Age is : ", c.age)
        print("My Gender is: ", c.gender)

c = person_1()
c.name = "Gokul"
c.age = 25
c.gender = "Male"
c.print_detials()