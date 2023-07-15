"""
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# Hybrid Inheritance is the mixture of two or more different types of inheritance. 
Here we can have many relationships between parent and child classes with multiple levels.
"""

class dog:
    def func1(self):
        print("Hello i'm dog")

class cat(dog):
    def func2(self):
        print("Hello i'm cat")
    
class elephant(dog):
    def func3(self):
        print("Hello i'm elephant")

class horse(cat, elephant):
    def func4(self):
        print("Hello i'm hourse")

"""
In Above program we used Single, Hirearchical, Multiple Inheritace concepts. So this is called 'Hybrid Inheritance'
Want to know more see in Notes.
""" 

hor_obj = horse()
hor_obj.func1()
hor_obj.func2()
hor_obj.func3()
hor_obj.func4()
print('\n')

class dog_1:
    def func1(self):
        print("Hello i'm dog_1")

class cat_1(dog_1):
    def func2(self):
        print("Hello i'm cat_1")
    
class elephant_1(cat_1):
    def func3(self):
        print("Hello i'm elephant_1")

class horse_1(elephant_1, dog_1):
    def func4(self):
        print("Hello i'm hourse_1")


hor_obj_1 = horse_1()
hor_obj_1.func1()
hor_obj_1.func2()
hor_obj_1.func3()
hor_obj_1.func4()


"""
In Above program we used Single, Multilevel, Multiple Inheritace concepts. So this is called 'Hybrid Inheritance'
Want to know more see in Notes.
""" 

















"""
Wants to know more,
https://www.scaler.com/topics/python/inheritance-in-python/
"""