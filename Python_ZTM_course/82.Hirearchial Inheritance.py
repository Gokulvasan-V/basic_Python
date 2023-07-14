"""
When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. 
In this program, we have a parent (base) class and two child (derived) classes.
"""

"""
Ex: Here, we are creating one(or)more derived classes for one base class
(Opposite of 'Multiple inheritance')
"""

class Parents_1:
    def parents_name(self):
        print("Father Name: Venkatachalam \nMother Name: Maheshwari")

class Child1(Parents_1):
    def child_name_1(self):
        print("1st child name: Keerthivasan")

class Child2(Parents_1):
    def child_name_2(self):
        print(f"1st child name: Gokulvasan")

c_1 = Child1()
c_1.parents_name()
c_1.child_name_1()
print('\n')

c_2 = Child2()
c_2.parents_name()
c_2.child_name_2()
print('\n')

print('#------------#------------#------------#------------#------------#', end='\n\n')


class Parents:
    def parents_name(self, father, mother):
        print(f"Father Name: {father} \nMother Name: {mother}")

class Child_1(Parents):
    def child_name_1(self,child_1):
        print(f"1st child name: {child_1}")

class Child_2(Parents):
    def child_name_2(self,child_2):
        print(f"1st child name: {child_2}")


child_1 = Child_1()
child_1.parents_name("Venkatachalam P", "Maheshwari V")
child_1.child_name_1("Keerthivasan V")
print('\n')

child_2 = Child_2()
child_2.parents_name("Venkatachalam P", "Maheshwari V")
child_2.child_name_2("Gokulvasan V")




"""
Want to know more,
https://www.geeksforgeeks.org/types-of-inheritance-python/
"""