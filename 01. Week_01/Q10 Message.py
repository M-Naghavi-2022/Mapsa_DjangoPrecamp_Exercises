
message = 'Babak Khorramdin'

# a
print(message[0])
print()

# b
print(message[6])
print()

# c
l = message.split()
print(l[0])
print(l[1])
print()

# d
for i in range(0,13,2):
    print(message[i])
print()

# e
flag = False
for i in message:
    if i == 'm':
        flag = True
        break
print(flag)