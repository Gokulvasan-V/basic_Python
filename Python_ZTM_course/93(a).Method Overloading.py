
# Another method for Method Overloadding

class a:
    def fun(self,*v):
        value = 0
        for i in v:
            value += i
        print("added value:", value)

obj = a()
obj.fun(10,20,30)
obj.fun(10,20,30,40)
obj.fun(10,20,30,40,50)

print('\n')
#-------------------#-------------------#-------------------#-------------------#

class area:
    def a(self, l=None, b=None):
        if(a!=None and b!=None and l!=b):
            print("Rectangle area:", l*b)
        else:
            print("Square area:", l*l)

ar = area()
ar.a(10, 30)
ar.a(60)
ar.a(20,20)
