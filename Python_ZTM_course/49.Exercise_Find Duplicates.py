List = ['a','b','c','b','d','m','n','n']

duplicates = []

for value in List:
    if List.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)