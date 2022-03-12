zz = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(zz)):
    if zz[i] % 2 == 0:
        print(zz[i],'div 2')
    if zz[i] % 3 == 0:
        print(zz[i], 'div 3')
        break

print('fim')