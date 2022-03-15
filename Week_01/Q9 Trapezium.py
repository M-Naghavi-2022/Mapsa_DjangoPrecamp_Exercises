length = int(input('Please Enter the length: '))
heigth = int(input('Please Enter the heigth: '))

for i in range(heigth):
    if i < heigth-1:
        print(' '*(heigth-1-i), end = '')

    if i == 0 or i == heigth-1:
        print('*'*length)
    else:
        print('*', end = '')
        print(' '*(length-2), end = '')
        print('*')