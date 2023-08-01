
class one:
    def name(self):
        print("I'm sakthi")
    def age(self):
        print("I'm 24 years old")
    def gender(self):
        print("Male")

class two:
    def name(self):
        print("I'm Sheela")
    def age(self):
        print("I'm 21 years old")
    def gender(self):
        print("Female")

obj_1 = one()
obj_2 = two()

for i in [obj_1, obj_2]:
    i.name()
    i.age()
    i.gender()
    print('\n')

#-------------------#-------------------#-------------------#-------------------#

# Polymorphism with a Function and Object.
# Here, we difine the object inside the function.
def func_call(obj):
    obj.name()
    obj.age()
    obj.gender()
    print('\n')


call_1 = func_call(obj_1)
call_2 = func_call(obj_2)


print('\n')
#-------------------#-------------------#-------------------#-------------------#

cls = [obj_1, obj_2]
cls[1].name()
cls[0].name()

