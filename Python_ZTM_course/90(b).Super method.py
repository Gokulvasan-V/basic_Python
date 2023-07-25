# here we will see 'super()' method in Multiple inheritance.

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
    def show(self):
        print("Full Employee detials")
        super().personal("Gokulvasan", 25, "Male")
        super().company("GVK Ltd", "Salem")
        super().others("10 LPA", "Data Science")
        


all = All_detials()
all.show()