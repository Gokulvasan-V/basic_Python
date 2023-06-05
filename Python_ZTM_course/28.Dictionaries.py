"""
In other languages, It might be called a hash table, maybe map or objects.
In Python, we have this idea of dictionary. Or as Python likes to call it, dict.
It's a data type in Python, but it's also a data structure.
"""

# it's a key & value pair.
dictionary = {
    'a' : 1,
    'b' : 2
} # key is a string for us to grab the value.

print(dictionary ['b']) # print by key.
print('\n')


dict_1 = {
    'm' : [1,2,3],
    'n' : 'hello',
    'o' : True,
    'p' : None
}

print(dict_1['m'])
print(dict_1['m'][1])
print(dict_1['n'])
print(dict_1['p'])
print('\n')


dict_2 = [{
    'm' : [1,2,3],
    'n' : 'hello',
    'o' : True,
    'p' : None
 },
 {
    'q' : [4,5,6],
    'r' : 'hii',
    's' : False,
    't' : None 
 }]

print(dict_2)
print(dict_2[0])
print(dict_2[1])
print(dict_2[0]['m'][1])
print(dict_2[1]['r'])



