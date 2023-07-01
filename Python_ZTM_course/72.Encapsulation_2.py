"""
Encapsulation Achive methods with using
Access Specifier:
1) public variable 
2) private variable
3) protect variable
"""

# 1) Public variable --> we can acess anywhere inside the class and outside the class.
class test:
    def detials(self, name, age):
        self.name = name
        self.age = age
        print('Name:', name) # here i accessing variable inside the function.
        print('Age:', age)    

obj = test()
obj.detials('Gokul', 23)
print('\n')

class test_2:
    def detials(self, name, age):
        self.name = name
        self.age = age

obj_2 = test_2()
obj_2.detials('GV', 24)
print('Name:', obj_2.name) # here i accessing variable globally.
print('Age:', obj_2.age)
print('\n')
# Both are working properly, there is no error while printing.


# 2) private variable --> we can access inside the function and class otherwise we can't access.

class test_3:
    def detials(self, name, age):
        self.__name = name
        self.__age = age
        print('Name:', self.__name) # here i accessing variable inside the function.
        print('Age:', self.__age)

obj_3 = test_3()
obj_3.detials("hello", 21)

print('Name:', obj_3.__name) # it will show error because we print globally.
print('Age:', obj_3.__age)