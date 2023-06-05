basket = [1,2,3,4,5,6,7]

print(len(basket))

print(basket[::-1])

"""
.join is actually something that works on strings.
It's a string method, but it's often used this way.
"""

sentence = '!'
sentence.join(['hii','my','name','is','jojo'])
print(sentence)

# in previous methods automatically stores in that perticular variable but .joint won't store.

new_join = sentence.join(['hii','my','name','is','jojo'])
print(new_join)

sentence_2 = ' '
new_join_2 = sentence_2.join(['hii','my','name','is','jojo'])
print(new_join_2)

# (or) we can use,

new_join_3 = ' '.join(['hii','my','name','is','jojo'])
print(new_join_3)