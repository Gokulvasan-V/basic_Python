"""
this is the same as the elseif or if else, statements.
But it's a shortcut (one line if and else).
So you can only use these on certain conditional logic.
these ternary operators can also be called conditional expressions.
"""

"""
condition_if_true if condition else condition_if_false. --> this is the logic of this statement.

in the above statement, "condition" is true means "condition_if_true" will work otherwise "condition_if_false" (else part) will work.
"""

is_friend = True
can_msg = 'msg allowed' if is_friend else "not allowed to messege"
print(can_msg) # here, "is_friend = True", so 'if' part will work change "is_friend = False" means 'else' part will work.


a = 19
b = 10
high_val = f'{a} is the highest value' if a>b else f'{b} is the highest value'
print(high_val)