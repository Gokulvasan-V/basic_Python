"""
when it comes to conditional logic, booleans are really, really important.
"""

is_old = True # if we change false means else part will work. 
is_licenced = True

if is_old:
    print("your old enough to drive")
else:
    print("you are not of age")

print("OK OK")

is_old_2 = False 
is_licenced_2 = True
# if is_old_2:
#     print("your old enough to drive") # old is True means if part will work.
# elif is_licenced_2:
#     print("You can drive now...!") # if we change old is False means 'elif' will work.
# else:
#     print("you are not of age") # both if and elif False means else part will run.

# print("OK OK")

is_old_3 = True
is_licenced_3 = True

# if is_old_3 and is_licenced_3:
#     print("your old enough to drive and you have a licence...!") # old is True means if part will work.
# else:
#     print("you are not of age") # both if and elif False means else part will run.

# print("OK OK\n")


is_old_4 = False
is_licenced_4 = True

# if is_old_4 and is_licenced_4:
#     print("your old enough to drive and you have a licence...!") # old is True means if part will work.
# elif is_licenced_4:
#     print('Your age is not enough')
# elif is_old_4:
#     print("'you don't have a licence")
# else:
#     print("you are not of age") # both if and elif False means else part will run.

# print("OK OK")
