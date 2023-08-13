"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 
"""

def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numbers = [1,2,3,4,5,6]
flt = filter(even, numbers)
print(list(flt))

#-------------------#-------------------#-------------------#-------------------#
print("\nUsing Lambda")

fun = filter(lambda x: x%2 == 0 , numbers)
print(list(fun))