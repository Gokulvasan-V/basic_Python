"""
this gives us information about the function by using doc strings.
"""

def test(a):
    '''
    Info: This function tests and prints perameter 'a'. 
    '''
    # The above line called 'Docstring'
    print(a)

test(75) # it will indicate our 'Docstring' Here.

help(test) # 'help' will show our information about 'test'.