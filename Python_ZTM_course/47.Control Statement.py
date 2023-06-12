"""
break --> Terminates the current loop statement and transfers execution to the statement immediately following the loop.
continue --> Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
pass --> The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
"""

str = "python"  
for i in str:  
    if i == 'o':  
        break  
    print(i)
print('\n')

for j in str:  
    if j == 'o':  
        continue  
    print(j)
print('\n')

for k in str:  
    if k == 'o':
        # i'm thinking about it.
        pass  
    #print(k)


# continue --> most commenly uses in for loop only
# break --> uses in both for and while
# pass --> uses in both for and while