
# If you have a knowledge on all inheritance concept then you see this one.

#  here we mainly focusing about MRO(Method Resolution Order).

class a:
    def a_func(self):
        print("Haii")

class b(a):
    def a_func(self):
        print("Hello")

obj = b()
obj.a_func() # It will print "Hello"

# this steps works based on "MRO" concept.

# MRO --> Method Resolution Order.

print(b.__mro__) # This Code will show order of the class methods.

print('\n')

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

#  here i'm creating new class inherite with 'b' class, 'b' class already inherited with 'a' class

class c(b): # Multi-level Inheritance.
    def a_func(self):
        print("I'm from 'c' Class")

obj = c()
obj.a_func()
print(c.__mro__)
print('\n')

#-----#-----#-----#-----#-----#-----#-----#-----#-----#

class d:
    def a_func(self):
        print("I'm from 'd' Class")

class e(a,d):
    pass

obj_2 = e()
obj_2.a_func() # it will print 'a' class.
print(e.__mro__) # afer "e" class, "a" is the 1st. that's why "a" class printing here