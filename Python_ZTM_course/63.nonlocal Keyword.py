# without 'nonlocal' keyword.
def outer():
    x = "local"
    def inner():
        x = "non-local"
        print("inner:",x)

    inner()
    print("outer:",x)

outer()
print('\n')

# with 'nonlocal' keyword.
def outer_2():
    x = "local"
    def inner():
        nonlocal x # nonlocal is a python keyword, it's converts into inner-local into local variable.
        x = "non-local"
        print("inner:",x)

    inner()
    print("outer:",x)

outer_2()

