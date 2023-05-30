'''
Index allows us to grab different pieces of text.
we can slice the string however we like.
'''

numbers=[0,1,2,3,4,5,6,7,8,9]
       # 0 1 2 3 4 5 6 7 8 9

#[start:stop]
print(numbers[0:2])
print(numbers[0:5])
print(numbers[0:9])
print(numbers[0:10])

#[start:stop:step over] here default stepover is 1
print(numbers[0:10:2])
print(numbers[1:10:2])
print(numbers[::2]) # starting at zero ending at whenever the string ends. here i gave only stepover.

# Nagative indexing

print(numbers[::-1]) # we get the reverse order.
print(numbers[::-2])
print(numbers[-2::-2])


# str1="hello everyone"
#     # 0123456789.....
# str2="Gokulvasan"

# print(type(str1))

# print (str1[4])
# print(str1[0:4]) #[start:stop]
# print (str1*2)
# print (str1 + str2)

# # in python only we have negative indexing
# print(str1[-2])
# print(str2[-6:-2])