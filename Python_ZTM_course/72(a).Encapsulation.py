# Private methods

class school:
    def detials(self):
        self.name = "ABC school"
        print("School Name:", self.name)
    def __stud1(self): # private method
        print("Name: Sakthi")
        print("Class: 10th")
    def stud2(self):
        self.__stud1() # we can access private method inside the public method
        print('\n')
        print("School Name:", self.name)
        print("Name: Shiva")
        print("Class: 12th")

obj = school()
obj.detials()
obj.stud2()


print('\n')
#-------------------#-------------------#-------------------#-------------------#

# we have only private methods

class school_1:
    def detials(self):
        self.name = "XYZ school"
        print("School Name:", self.name)
    def __stud1(self): # private method
        print("Name: Sakthi")
        print("Class: 10th")
    def __stud2(self):
        self.__stud1() # we can access private method inside the public method
        print('\n')
        print("School Name:", self.name)
        print("Name: Shiva")
        print("Class: 12th")

obj_1 = school_1()
obj_1.detials()
obj_1._school_1__stud1() # Name mangling --> acessing private variable (or) method.
obj_1._school_1__stud2()



"""
NOTE:
----
Accessing private Variable/ Method:
1) through public method
2) through name mangling
"""