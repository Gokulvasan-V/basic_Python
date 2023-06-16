def PrintSum(n1,n2):
    sum = n1 + n2
    print(sum)

def ReturnSum(n1,n2):
    sum = n1 + n2
    return sum

# print --> It is only print the result can't store anywhere.
#PrintSum(1,2)
a = PrintSum(1,3)
print(a)
print("\n")

# return --> Won't print, when we store then only it will print.
ReturnSum(2,5)

b= ReturnSum(3,7)
print(b)

