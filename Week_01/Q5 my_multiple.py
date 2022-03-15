def my_multiple(x,y):
    i = 1
    sum = 0
    while i <= y:
        sum += x
        i += 1
    return sum

x = int(input('Please Enter x: '))
y = int(input('Please Enter y: '))

print(my_multiple(x, y))