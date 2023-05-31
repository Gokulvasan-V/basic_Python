
"""
Like strings, lists are quite similar in that we can use list slicing.
"""

amazon_cart = ['note books', 'suunglasses', 'toys', 'mango']

print(amazon_cart,'\n',len(amazon_cart))

print(amazon_cart[0:3])
print(amazon_cart[0::2])

"""
List are mutable
"""
amazon_cart[1] = 'laptops'
print(amazon_cart)