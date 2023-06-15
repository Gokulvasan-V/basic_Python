"""
A return keyword automatically exits the function
"""

def sum(num1 ,num2):
    return num1 + num2

print(sum(5,8))
print('\n')

# if we didn't use return statement means

def sum1(num1, num2):
    print('hello')
    print(num1 + num2)

sum1(10,5)
print('\n')

def sum2(num1, num2):
    def another_func(n1, n2):
        return num1 + num2
    return another_func(num1, num2)

total = sum2(10,30)
print(total)