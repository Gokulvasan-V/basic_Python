# 'Yield' also like an iterator.

def num():
    yield 5

obj = num()
print(obj) # Generator object
print(obj.__next__())
# print(obj.__next__()) # it will show "StopIteration"


print('\n')
#-------------------#-------------------#-------------------#-------------------#

def num1():
    yield 10
    yield 9
    yield 8
    yield 7
    yield 6
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

obj_1 = num1()
print(obj_1.__next__())
print(obj_1.__next__())
print(obj_1.__next__())
print(obj_1.__next__())
print(obj_1.__next__())

# Both are same code (above and below)
print(next(obj_1))
print(next(obj_1))
print(next(obj_1))
print(next(obj_1))
print(next(obj_1))

# print(obj.__next__()) # it will show "StopIteration"

print('\nUsing for loop:')
#-------------------#-------------------#-------------------#-------------------#

def num2():
    yield 10
    yield 9
    yield 8
    yield 7
    yield 6
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

obj_2 = num2()

for i in obj_2:
    print(i)

print('\nWithout Function calling:')
#-------------------#-------------------#-------------------#-------------------#

def num3():
    yield 10
    yield 9
    yield 8
    yield 7
    yield 6
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

for i in num3():
    print(i)