for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = '  ')
        if i*j < 10:
            print(' ', end = '')
    print()