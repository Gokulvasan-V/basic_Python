# maximum even number
def highest_even(li):
    even_max = []
    for item in li:
        if item %2 == 0:
            even_max.append(item)
            #print(even_max)
    return max(even_max)

print(highest_even([10,2,3,4,8,11]))

# minimum even number

def lowest_even(li_1):
    even_min = []
    for item in li_1:
        if item%2 == 0:
            even_min.append(item)
            #print(even_min)
    return min(even_min)
    
print(lowest_even([10,2,3,4,8,11]))
