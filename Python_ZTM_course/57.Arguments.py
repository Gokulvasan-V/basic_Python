# *args and **kwargs

# def super_func(args):
#     return sum(args)

# super_func(1,2,3,4,5,6,7,8,9) # if we run this it will show error, because we gave 9 arguments.


# *args --> this can accept any number of positional arguments like above. As many as I want.
def super_func_2(*args): # in 'args' place we can give any name with star(*). but 'args' is the most standard name.
    print(args)
    return sum(args)

a = super_func_2(1,2,3,4,5,6,7,8,9) # because we ued 'return', that's why we stored in a variable.
print(a)
print('\n')

# **kwargs --> we can give by kay and value.

def kwarg(**kwargs):
    print(kwargs)

kwarg(num=1, num_2=2, num_3=3) # it will store like 'Dict' format.
print('\n')

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
        print(total)
    return sum(args) + total

print(super_func(1,2,3,4,5,6,7, num1=5,num2=7))