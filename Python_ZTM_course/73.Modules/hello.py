
"""
A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. 
A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. 
It also makes the code logically organized.
"""

def test():
    print("This is from 'hello.py' file")

def test_2():
    a = int(input("Enter the mark: "))
    if a<=100 and a>=80:
        print('A grade')
        if a == 100:
            print('v.good')
        elif a == 99:
            print('good')
        else:
            print('next time get 100')
    elif a<=81 and a>=60:
        print('B grade')
    elif a<=61 and a>=40:
        print('C grade')
    elif a<40 and a>=0:
        print('Fail')
    else:
        print('invalid input')