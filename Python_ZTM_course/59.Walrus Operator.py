"""
Walrus Operator is an Assignment expressions
There is new syntax ':=' that assigns values to variables as part of a larger expression. 
It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.
"""

a = 'helloooooooooo'

# if ((n = len(a)) > 10): # we can't store value in variable in the place of expression.
#     print(f"too long {n} elements") #it will show error

if ((n := len(a)) > 10): # Walrus Operator can resolve above problem.
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)


"""
Want to know more,
https://docs.python.org/3/whatsnew/3.8.html
"""