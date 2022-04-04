num_1 = int(input('Please Enter the 1st number: '))
num_2 = int(input('Please Enter the 2nd number: '))
num_3 = int(input('Please Enter the 3rd number: '))

min = num_1
max = num_1

if num_2 < min:
    min = num_2
if num_2 > max:
    max = num_2

if num_3 < min:
    min = num_3
if num_3 > max:
    max = num_3

print('max is: ', max)
print('min is: ', min)