
"""
Logical Operators:

1) and
2) or 
3) not
"""

"""
it allows us to perform logic between two things.
"""

is_magician = False
is_expert = True

# check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("You are a master magician")

# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")

# if you're not a magician: 
elif not is_magician:
    print("You need magic powers")