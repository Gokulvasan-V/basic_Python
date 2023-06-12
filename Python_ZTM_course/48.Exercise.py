
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for i in picture:
    for pixcel in i:
        if pixcel == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
