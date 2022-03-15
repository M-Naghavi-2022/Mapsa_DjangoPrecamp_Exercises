import random
rand_num = random.randint(1,20)

for i in range(5):
    user_num = int(input('Please Enter a Number 1~20: '))
    if user_num == rand_num:
        print('You Win! ', user_num, 'is correct')
        break
else:
    print('Game Over!  The correct number is', rand_num)