"""
When a class is derived from more than one base class it is called multiple Inheritance.
The derived class inherits all the features of the base case.
"""

"""
Ex: We are creating derived class for two base classes
"""

class Personal_detials: # Base (or) Parent class
    def personal(self, name, age, gender):
        print(f"Name: {name} {'-'*5} age: {age} {'-'*5} Gender: {gender}")

class Company_detials: # Base class (or) Parent class
    def company (self, c_name, c_location):
        print(f"Company Name: {c_name} {'-'*5} Company location: {c_location}")

class other_detials: # Base class (or) Parent class
    def others(self, salary, desgnation):
        print(f"Salary: {salary} {'-'*5} Designation: {desgnation}")

# Multiple Inheritance class
class All_detials(Personal_detials, Company_detials, other_detials): # Derived (or) Child class
    print("Full Employee detials")


p = Personal_detials()
p.personal("Gokul", 24, "Male")

c = Company_detials()
c.company("GV Ltd", "Salem")

o = other_detials()
o.others("8 LPA", "Data Analysis")

print("\n")
print("This is from 'Multiple Inheritance' class")
all = All_detials()
all.personal("Gokulvasan", 25, "Male")
all.company("GVK Ltd", "Erode")
all.others("10 LPA", "Data Science")




"""
Want to know more
https://www.geeksforgeeks.org/multiple-inheritance-in-python/
"""