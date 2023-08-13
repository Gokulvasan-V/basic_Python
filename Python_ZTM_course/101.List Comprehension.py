"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
"""

letters = []

for i in "HUMAN":
    letters.append(i)

print(letters)

#-------------------#-------------------#-------------------#-------------------#
print("\nUsing List Comprehension:")

letter = [ x for x in "HUMAN"]
print(letter)

#-------------------#-------------------#-------------------#-------------------#
print("\n")

print([ x for x in range(1,11)])

#-------------------#-------------------#-------------------#-------------------#
print("\n")

print([ x for x in range(1,11) if x%2 == 0 ])

#-------------------#-------------------#-------------------#-------------------#
print("\n")

re = ["even" if x%2 == 0 else "odd" for x in range(1,12)]
print(re)