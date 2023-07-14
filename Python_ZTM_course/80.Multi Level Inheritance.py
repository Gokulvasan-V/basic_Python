"""
In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
This is similar to a relationship representing a child and a grandfather.
"""

class one:
    def func_1(self):
        print("I am from class 'One'")
    
class two(one): # child class of 'One'
    def func_2(self):
        print("I am from class 'Two'")

class three(two): # child class of 'Two'
    def func_3(self):
        print("I am from class 'Three'")

obj = three() # Here, i created object for 'three'(child) class
obj.func_1()
obj.func_2()
obj.func_3()
print("\n")
#-----------#-----------#-----------#-----------#-----------#-----------#
"""
Example:
    we creating employee data by three classes.
"""

class personal_data: # Parent class
    # def __init__(self, name, age, gender):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    
    def personal(self, name, age, gender):
        print(f'Employee name: {name}\nEmployee age: {age}\nEmployee gender: {gender}')

class company_data(personal_data):# child class of "personal_data"
    # def __init__(self, c_name, c_location):
    #     self.c_name = c_name
    #     self.c_location = c_location

    def company_detials(self, c_name, c_location):
        print(f"Company name: {c_name}. \nCompany location: {c_location}")

class private_data(company_data): # child class of "company_data"
    # def __init__(self, salary, designation):
    #     self.salary = salary
    #     self.designation = designation

    def private(self,salary, designation):
        print(f"Salary: {salary}. \nDesignation: {designation}")

employee_data = private_data()

employee_data.personal("Gokulvasan V", 24, "Male")
employee_data.company_detials("IT", "Salem")
employee_data.private(50000, "Software Developer")
print('\n')

# Here, I'm accessing company_data class only
company = company_data() # We cn access separately 'company' class 
company.company_detials("GK group of Company", "Erode")
company.personal("Master", 42, "Female")
#company.private(70000, "Master") # it will show error because we didn't inherite 'private' class in the 'company' class
