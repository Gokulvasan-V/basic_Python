"""
Short-circuiting in Python is a technique by which execution of boolean expression containing 
'or' and 'and' operator in Python is halted as soon as the truth value of the expression is determined.
"""

is_friend = True
is_user = True

if is_friend and is_user:
    print("best friends forever")

is_friend_2 = True
is_user_2 = False

if is_friend_2 or is_user_2:
    print("best friends forever")