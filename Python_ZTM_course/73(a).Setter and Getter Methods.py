
# Setter and Getter Methods using '@property' decorator.

class demo:
    def __init__(self):
        self._age = 0
    
    # getter
    @property  #decorator
    def age(self):
        print("getter method called")
        return self._age # here you must give same for attribute and method names 

    # setter
    @age.setter # here 'age' is method
    def age(self, a):
        if a<18:
            print("You are below 18")
        else:
            print("You are above 18")

        print("Setter method called")
        self._age = a

obj = demo()
obj.age = 20 # age method
print(obj.age)

print('\n')

obj = demo()
obj.age = 15 # age method
print(obj.age)