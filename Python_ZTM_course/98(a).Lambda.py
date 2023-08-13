# Lambda - User Defined Function

x = lambda a,b,c : a+b+c
print(x(5,6,7))

print('\n')
#-------------------#-------------------#-------------------#-------------------#

# with default argument 
y = lambda a,b=30,c=20 : a+b+c
print(y(20)) # a=20
print(y(20,40)) # a=20, b=40
print(y(20,40,30))

print("\nUsing \"*args\"")
#-------------------#-------------------#-------------------#-------------------#

add = lambda *args : sum(args)
print(add(10,20,30,40,50))
print(add(10,20,30,40,50,60))

print("\nImediate invoke function")
#-------------------#-------------------#-------------------#-------------------#

# Imediate invoke function
print((lambda a,b : a*b)(10,20))

print("\n")
#-------------------#-------------------#-------------------#-------------------#

l1 = [1,2,3,4,5]
l2 = []

for i in l1:
    temp = lambda i:i**2
    l2.append(temp(i))

print(l2)