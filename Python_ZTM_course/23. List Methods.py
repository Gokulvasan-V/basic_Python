basket = [1,2,3,4,5,6,7,8]

print(basket)
print(len(basket))

#append --> adding the value at the end of the List
new_list=basket
new_list.append(9)
print(new_list)

# insert --> add value, which place we want
new_list2=basket
new_list2.insert(0,10) #(index, value)
print(new_list2)

print('\n')
print(new_list)
print(basket)
print(new_list2)
print('\n')

# extend --> adding multiple elements at the end of the list.

basket.extend([100,200,300])
print(basket)

print('\n')

# pop --> remove defaultly end of the element

basket.pop()
print(basket)

basket.pop(3) # here we can give index value.
print(basket)

print('\n')

# clear --> remove all elements.

basket.clear()
print(basket)


"""
want to know more methods,
https://www.w3schools.com/python/python_ref_list.asp
"""