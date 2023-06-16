def is_even():
    num = int(input("Enter the number: "))
    #rint(num)
    if num % 2 ==0:
        print("Even number")
    else:
        print("not even number")

#is_even()


# (or)

def is_even_2():
    num_1 = int(input("Enter the number: "))
    #print(num_1)
    return num_1 % 2 == 0 

print(is_even_2()) # It will return 'True (or) False'.