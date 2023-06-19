b = 7 
def counter():
    a = 5
    return a+b

print(counter())

# print(a) # it will shoe error because it is a local scope.
print('\n')

def counte_2():
    global c # global is a python keyword. it converts to local into global.
    c = 8
    return c+b

print(counte_2())
print(c)