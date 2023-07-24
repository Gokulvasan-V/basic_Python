
# We can't use "return" inside the constructor.

# Normal Return code 

class add:
    def a(self, a, b):
        c = a+b
        return c
    
add_1 = add()
print(add_1.a(6,9))

# Constructor with Return

class test:
    def __init__(self):
        a = "Sakthi"
        return a
    
# obj = test() # ERROR --> Construtor doesn't return string, integer and etc, It returns only 'NONE' type.
print('\n')

class person:
    name = "John"
    def __init__(self):
        name = "Sakthi"
        print(name)

obj = person() # Here, 'John' overwritted