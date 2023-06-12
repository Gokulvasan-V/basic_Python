"""
when should you use a while loop and when should you use a for loop...?
    >> it really depends on the problem you're trying to solve.
    >> let's say you're not sure how many times you want to loop over something.
"""

for item in [1,2,3,4]:
    print(item)
print('\n')

i = 0
while i < len([1,2,3,4]):
    print(i)
    i += 1
print('\n')

while True:
    resopnce = input('Say somethings: ')
    if resopnce == 'bye' or resopnce == 'Bye' or resopnce == 'BYE':
        print("program stoped")
        break