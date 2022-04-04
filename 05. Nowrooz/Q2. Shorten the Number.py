def shorten(num):
    max = 0
    for i in range(len(num)-1):
        add = str(int(num[i])+int(num[i+1]))            # adds two neighbor digits
        shorted_num = int(num[:i] + add + num[i+2:])    # forms the shorted number and converts it to int
        if shorted_num >= max:
            max = shorted_num

    print(max)


in_num = input()
shorten(in_num)
