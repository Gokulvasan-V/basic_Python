
basket = [1,2,3,4,5,6,7]

print(basket.index(2)) # it will show index No.of 3

basket_1 = ['a','b','c','d','e']
print(basket_1.index('c')) # it will show index No.of 'c'

# print(basket_1.index('e',0,3)) # here we set a limit from 0 to 3, in the list program will look only till 0 to 3.

print(basket_1.index('e',0,5)) # here we set a limit from 0 to 3, in the list program will look only till 0 to 3.

print('c' in basket_1)

print('x' in basket_1)

print(basket_1.count('d'))

basket_1.append('d')
print(basket_1)

print(basket_1.count('d'))

basket_1_2 = basket_1.copy()
print(basket_1_2)

basket_1.sort() # it will sort assending order
print(basket_1)

basket_2 = basket_1
print(basket_2) # it will show the sorted OP, because both variables are same. will we change again 'basket_1' means that will also reflect in 'basket_2'

basket_1.reverse() # it won't print by assending order it will print by index.
print(basket_1)
print(basket_2)
